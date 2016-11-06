# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 15:48:10 2016

@author: Lathropk
"""
from django.conf import settings
import sqlalchemy as sa
from sqlalchemy import MetaData, Table, select, case, cast, Date, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import and_


Base = declarative_base()
oasis_engine = settings.OASIS_ENGINE
metadata = MetaData(oasis_engine)
metadata.reflect(only=['CDS_SlotMast',
                       'BB_SlotType',
                       'BB_MFR',
                       'BB_CABINET',
                       'BB_PROGRESSIVETYPE',
                       'BB_STYLE',
                       'BB_REVENUE',
                       'BB_Revenue_PBT'
                       ])
connection = oasis_engine.connect()

SlotMast = metadata.tables['CDS_SlotMast']
SlotType = metadata.tables['BB_SlotType']
Mfr = metadata.tables['BB_MFR']
Cabinet = metadata.tables['BB_CABINET']
ProgressiveType = metadata.tables['BB_PROGRESSIVETYPE']
Style = metadata.tables['BB_STYLE']
Revenue = metadata.tables['BB_REVENUE']
RevenuePBT = metadata.tables['BB_Revenue_PBT']

class RevisionHistory(Base):
    __tablename__ = 'revision_history'
    __table__ = Table('BB_REVISIONHISTORY', metadata, autoload=True)


def game_update(audit_date):
    
    #fix for decimal problem
    for column in SlotMast.columns.values():
        if isinstance(column.type, sa.Numeric):
            column.type.asdecimal = False

    s = select([SlotMast.c.SlotNumber.label('slot_number'),
                SlotMast.c.EditDate.label('edit_date'),
                Style.c.StyleDesc.label('game_type'),
                SlotMast.c.Denomination.label('denomination'),
                SlotMast.c.Description.label('description'),
                Cabinet.c.CabinetDesc.label('cabinet'),
                SlotMast.c.Par.label('par'),
                SlotMast.c.nReels.label('num_reels'),
                SlotMast.c.nPaylines.label('num_paylines'),
                SlotMast.c.nCoins.label('num_coins'),
                case([(SlotMast.c.ProgressiveType_ID == None, False)], else_=True).label('progressive'),
                Mfr.c.Manufacturer.label('manufacturer'),
                case([(SlotType.c.Style_ID == 5, True)], else_=False).label('multigame'),
                case([(SlotType.c.MultiDenomination == None, False)], else_=True).label('multidenom'), 
                ])
                 
    s = s.select_from(SlotMast.outerjoin(SlotType, 
                                    SlotMast.c.SlotType_ID == SlotType.c.SlotType_ID,
                                    )\
                             .outerjoin(Style, SlotMast.c.Style_ID == Style.c.Style_ID)\
                             .outerjoin(Mfr, SlotType.c.Mfr_ID == Mfr.c.Mfr_ID)\
                             .outerjoin(Cabinet, SlotMast.c.Cabinet_ID == Cabinet.c.Cabinet_ID)\
                             )             
    s = s.where(cast(SlotMast.c.EditDate, Date) == audit_date)
    
    s = s.order_by(SlotMast.c.EditDate)
                     
    rp = connection.execute(s)
    resultset = [dict(row) for row in rp]
    
    return resultset

def game_load():

    s = select([SlotMast.c.SlotNumber.label('slot_number'),
                SlotMast.c.EditDate.label('edit_date'),
                Style.c.StyleDesc.label('game_type'),
                cast(SlotMast.c.Denomination, Float).label('denomination'),
                SlotMast.c.Description.label('description'),
                Cabinet.c.CabinetDesc.label('cabinet'),
                cast(SlotMast.c.Par, Float).label('par'),
                SlotMast.c.nReels.label('num_reels'),
                SlotMast.c.nPaylines.label('num_paylines'),
                SlotMast.c.nCoins.label('num_coins'),
                case([(SlotMast.c.ProgressiveType_ID == None, False)], else_=True).label('progressive'),
                Mfr.c.Manufacturer.label('manufacturer'),
                case([(SlotType.c.Style_ID == 5, True)], else_=False).label('multigame'),
                case([(SlotType.c.MultiDenomination == None, False)], else_=True).label('multidenom'), 
                ])
                 
    s = s.select_from(SlotMast.outerjoin(SlotType, 
                                    SlotMast.c.SlotType_ID == SlotType.c.SlotType_ID,
                                    )\
                             .outerjoin(Style, SlotMast.c.Style_ID == Style.c.Style_ID)\
                             .outerjoin(Mfr, SlotType.c.Mfr_ID == Mfr.c.Mfr_ID)\
                             .outerjoin(Cabinet, SlotMast.c.Cabinet_ID == Cabinet.c.Cabinet_ID)\
                             )             
    
    s = s.order_by(SlotMast.c.EditDate)
                     
    rp = connection.execute(s)
    resultset = [dict(row) for row in rp]
    
    return resultset

def slot_revenue(audit_date):
    
    s = select([SlotMast.c.SlotNumber,
                (SlotMast.c.CasinoCode).label('casino'),
                (SlotMast.c.Area).label('area'),
                (SlotMast.c.Section).label('section'),
                (SlotMast.c.Loc).label('position'),
                Revenue.c.AuditDate,
                (Revenue.c.ElecCoinIn).label('CoinIn'),
                (Revenue.c.GameStart).label('GamesPlayed'),
                (Revenue.c.ElecCoinIn * (SlotMast.c.Par / 100)).label('TheoWin'),
                ((Revenue.c.ElecCoinDrop +
                 Revenue.c.CoinDropVar +
                 Revenue.c.MeteredBillIn +
                 Revenue.c.BillInVar +
                 Revenue.c.MeteredVoucherIn +
                 Revenue.c.VoucherInVar +
                 RevenuePBT.c.PromoDownMan) - (
                 Revenue.c.Fills + 
                 Revenue.c.ActualAttPaidProg +
                 Revenue.c.ActualAttPaidExtBonus +
                 Revenue.c.Jackpots + 
                 Revenue.c.ManualTicketOut)).label('Gross Win'),
                 (case(
                      [
                       (SlotMast.c.Lease_ID == 0, 
                            SlotMast.c.ProgPC * 1),
                       (SlotMast.c.Lease_ID == 1, 
                            (SlotMast.c.ProgPC * 1) / 30),
                       (SlotMast.c.Lease_ID == 2, 
                            Revenue.c.ElecCoinIn * (SlotMast.c.ProgPC / 100)),
                       (SlotMast.c.Lease_ID == 3, 
                            (Revenue.c.ScaleDrop +
                            Revenue.c.ManualBillDrop +
                            Revenue.c.ManualTicketDrop) *                 
                            (SlotMast.c.ProgPC / 100)),
                       (SlotMast.c.Lease_ID == 4,
                            (((Revenue.c.ElecCoinDrop +
                               Revenue.c.CoinDropVar +
                               Revenue.c.MeteredBillIn +
                               Revenue.c.BillInVar +
                               Revenue.c.MeteredVoucherIn +
                               Revenue.c.VoucherInVar +
                               RevenuePBT.c.PromoDownMan) - (
                               Revenue.c.Fills + 
                               Revenue.c.ActualAttPaidProg +
                               Revenue.c.ActualAttPaidExtBonus +
                               Revenue.c.Jackpots + 
                               Revenue.c.ManualTicketOut)) * 
                               (SlotMast.c.ProgPC / 100)))
                      ],
                     else_=0)).label('LeaseFee'),
                (RevenuePBT.c.PromoDownMan).label('Promo Play'),
                (Revenue.c.Jackpots).label('Jackpots'),
               ])
                      
    s = s.select_from(Revenue.outerjoin(RevisionHistory,
                     and_(
                          Revenue.c.SlotMast_ID == RevisionHistory.SlotMast_ID,
                          Revenue.c.AuditDate == RevisionHistory.AuditDate,
                          ))\
                
                .outerjoin(SlotMast, 
                       and_(
                           RevisionHistory.SlotMast_ID == SlotMast.c.SlotMast_ID,
                           RevisionHistory.Revision == SlotMast.c.Revision,
                           ))\
                .outerjoin(RevenuePBT, 
                       and_(
                           RevisionHistory.SlotMast_ID == RevenuePBT.c.SlotMast_ID,
                           RevenuePBT.c.AuditDate == Revenue.c.AuditDate,
                           RevenuePBT.c.Period_ID == Revenue.c.Period_ID,
                           )))
                   
    s = s.where(and_(Revenue.c.AuditDate == audit_date, 
                     Revenue.c.Period_ID == 4,
                     Revenue.c.DaysOnLine > 0)
                 )
                 
    rp = connection.execute(s)
    resultset = [dict(row) for row in rp]
    
    return resultset


# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 09:59:54 2016

@author: Lathropk
"""
import datetime
from dateutil.parser import parse
from django.conf import settings
from sqlalchemy import Table, MetaData, select, Float, Date, Numeric, case
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import and_, functions
from sqlalchemy.sql.expression import cast
from utils.loggers import ExtractLogger

Base = declarative_base()
oasis_engine = settings.OASIS_ENGINE
metadata = MetaData(bind=oasis_engine)
metadata.reflect(only=['CDS_SlotMast',
                       'CDS_StatTrip',
                       'CDS_StatTripDetail',
                       'CDS_StatDetail',
                       'BB_SlotType',
                       'BB_MFR',
                       'BB_CABINET',
                       'BB_PROGRESSIVETYPE',
                       'BB_STYLE',
                       'BB_REVENUE',
                       'BB_Revenue_PBT',
                       'CDS_Player', 
                       'PlayerAddress',
                       'CDS_Group',
                       'CDS_GroupEnroll',
                       'CDS_USER',
                       'PB_Location',
                       'PB_DROP',
                       'PB_RevenueDTD',
                       'HC_PRIME_REPORTDATA',
                       ])
connection = oasis_engine.connect()

DecBase = declarative_base()

class RevisionHistory_(DecBase):
    __tablename__ = 'revision_history'
    __table__ = Table('BB_REVISIONHISTORY', metadata, autoload=True)


SlotMast = metadata.tables['CDS_SlotMast']
Trip = metadata.tables['CDS_StatTrip']
TripDetail = metadata.tables['CDS_StatTripDetail']
SessionDetail = metadata.tables['CDS_StatDetail']
RevisionHistory = metadata.tables['BB_REVISIONHISTORY']
SlotType = metadata.tables['BB_SlotType']
Mfr = metadata.tables['BB_MFR']
Cabinet = metadata.tables['BB_CABINET']
ProgressiveType = metadata.tables['BB_PROGRESSIVETYPE']
Style = metadata.tables['BB_STYLE']
Revenue = metadata.tables['BB_REVENUE']
RevenuePBT = metadata.tables['BB_Revenue_PBT']
Player = metadata.tables['CDS_Player']
Address = metadata.tables['PlayerAddress']
Group = metadata.tables['CDS_Group']
GroupEnroll = metadata.tables['CDS_GroupEnroll']
Employee = metadata.tables['CDS_USER']
PitLocation = metadata.tables['PB_Location']
TableDrop = metadata.tables['PB_DROP']
TableRevenue = metadata.tables['PB_RevenueDTD']
Headcount = metadata.tables['HC_PRIME_REPORTDATA']

logger = ExtractLogger()
extract_logger = logger.myLogger()


def slot_session_extract(audit_date):
    extract_logger.info("Extracting slot player session records for %s" %audit_date )
    s = select([SlotMast.c.CasinoCode,
                SlotMast.c.Area,
                SlotMast.c.Section,
                SlotMast.c.Loc,
                SessionDetail.c.Detail_ID.label('session_id'),
                SessionDetail.c.Meta_ID.label('player_id'),
                SessionDetail.c.StatType.label('session_type'),
                SessionDetail.c.SlotNumber.label('slot_number'),
                SessionDetail.c.Location.label('game'),
                SessionDetail.c.Pit.label('pit'),
                SessionDetail.c.Shift_ID.label('shift'),
                SessionDetail.c.GamingDate.label('gaming_date'),
                SessionDetail.c.StartTime.label('start_time'),
                SessionDetail.c.TimePlayed.label('time_played'),
                cast(SessionDetail.c.CashIn, Float).label('cash_in'),
                cast(SessionDetail.c.CashOut, Float).label('cash_out'),
                cast(SessionDetail.c.JackPot, Float).label('jackpots'),
                cast(SessionDetail.c.TWin, Float).label('theo_win'),
                cast(SessionDetail.c.PromoPlay, Float).label('freeplay'),
                ])
    
    s = s.select_from(SlotMast.join(SessionDetail, 
                                    SessionDetail.c.SlotNumber == SlotMast.c.SlotNumber)\
                              .join(RevisionHistory, 
                                   and_(
                                       RevisionHistory.c.SlotMast_ID == SlotMast.c.SlotMast_ID,
                                       RevisionHistory.c.Revision == SlotMast.c.Revision,
                                       RevisionHistory.c.AuditDate == audit_date,
                                       )))
    
    s = s.where(SessionDetail.c.GamingDate == audit_date)
                     
    s = s.order_by(SessionDetail.c.Detail_ID)
    
    try:                 
        rp = connection.execute(s)
        resultset = [dict(row) for row in rp]
        extract_logger.info("Extract successful")
        return resultset
        
    except Exception, e:
            extract_logger.info("Error extracting slot player session data for %s" %audit_date)
            extract_logger.error(e, exec_info=True)

def pit_session_extract(audit_date):
    extract_logger.info("Extracting pit player session records for %s" %audit_date )
    s = select([SessionDetail.c.Detail_ID.label('session_id'),
                SessionDetail.c.Meta_ID.label('player_id'),
                SessionDetail.c.StatType.label('session_type'),
                SessionDetail.c.Location.label('location'),
                SessionDetail.c.Location.label('game'),
                SessionDetail.c.Pit.label('pit'),
                SessionDetail.c.Shift_ID.label('shift'),
                SessionDetail.c.GamingDate.label('gaming_date'),
                SessionDetail.c.StartTime.label('start_time'),
                SessionDetail.c.TimePlayed.label('time_played'),
                SessionDetail.c.PlayerSkill.label('player_skill'),
                SessionDetail.c.PlayerSpeed.label('player_speed'),
                cast(SessionDetail.c.CashIn, Float).label('cash_in'),
                cast(SessionDetail.c.ChipsIn, Float).label('chips_in'),
                cast(SessionDetail.c.CashOut, Float).label('cash_out'),
                cast(SessionDetail.c.JackPot, Float).label('jackpots'),
                cast(SessionDetail.c.TWin, Float).label('theo_win'),
                cast(SessionDetail.c.PromoPlay, Float).label('freeplay'),
                SessionDetail.c.RatedByUser_ID.label('rated_by'),
                ])
    
    s = s.select_from(SessionDetail)
    
    s = s.where(and_(SessionDetail.c.GamingDate == audit_date,
                     SessionDetail.c.StatType == 'PIT'))
                     
    s = s.order_by(SessionDetail.c.Detail_ID)
    
    try:                 
        rp = connection.execute(s)
        resultset = [dict(row) for row in rp]
        extract_logger.info("Extract successful")
        return resultset
        
    except Exception, e:
            extract_logger.info("Error extracting player session data for %s" %audit_date)
            extract_logger.error(e, exec_info=True)

def slot_trip_extract(audit_date):
    extract_logger.info("Extracting slot player trip records for %s" % audit_date )
    s = select([Trip.c.StatTrip_ID.label('trip_id'),
                Trip.c.Meta_ID.label('player_id'),
                Trip.c.StartGamingDate.label('start_date'),
                Trip.c.EndGamingDate.label('end_date'),
                TripDetail.c.StatType.label('trip_type'),
                TripDetail.c.TimePlayed.label('time_played'),
                cast(TripDetail.c.CashIn, Float).label('cash_in'),
                cast(TripDetail.c.CashOut, Float).label('cash_out'),
                cast(TripDetail.c.JackPot, Float).label('jackpots'),
                cast(TripDetail.c.TWin, Float).label('theo_win'),
                cast(TripDetail.c.PromoPlay, Float).label('freeplay'),
                ])
    
    s = s.select_from(Trip.join(TripDetail, 
                                    Trip.c.StatTrip_ID == TripDetail.c.StatTrip_ID))
    
    s = s.where(and_(Trip.c.EndGamingDate == audit_date,
                     TripDetail.c.StatType == 'SLOT'))
                     
    s = s.order_by(Trip.c.EndGamingDate)
                     
    try:                 
        rp = connection.execute(s)
        resultset = [dict(row) for row in rp]
        extract_logger.info("Extract successful")
        return resultset
        
    except Exception, e:
            extract_logger.info("Error extracting player trip data for %s" % audit_date)
            extract_logger.exception(e)

def pit_trip_extract(audit_date):
    extract_logger.info("Extracting pit player trip records for %s" % audit_date )
    s = select([Trip.c.StatTrip_ID.label('trip_id'),
                Trip.c.Meta_ID.label('player_id'),
                Trip.c.StartGamingDate.label('start_date'),
                Trip.c.EndGamingDate.label('end_date'),
                TripDetail.c.StatType.label('trip_type'),
                TripDetail.c.TimePlayed.label('time_played'),
                cast(TripDetail.c.CashIn, Float).label('cash_in'),
                cast(TripDetail.c.ChipsIn, Float).label('chips_in'),
                cast(TripDetail.c.CashOut, Float).label('cash_out'),
                cast(TripDetail.c.JackPot, Float).label('jackpots'),
                cast(TripDetail.c.TWin, Float).label('theo_win'),
                cast(TripDetail.c.PromoPlay, Float).label('freeplay'),
                ])
    
    s = s.select_from(Trip.join(TripDetail, 
                                    Trip.c.StatTrip_ID == TripDetail.c.StatTrip_ID))
    
    s = s.where(and_(Trip.c.EndGamingDate == audit_date,
                     TripDetail.c.StatType == 'PIT'))
                     
    s = s.order_by(Trip.c.EndGamingDate)
                     
    try:                 
        rp = connection.execute(s)
        resultset = [dict(row) for row in rp]
        extract_logger.info("Extract successful")
        return resultset
        
    except Exception, e:
            extract_logger.info("Error extracting pit player trip data for %s" % audit_date)
            extract_logger.exception(e)
    

def player_extract(audit_date, player_id=None):
    s = select([Player.c.Player_ID.label('player_id'),
                Player.c.Timestamp.label('player_timestamp'),
                Player.c.EntryDate.label('date_joined'),
                Player.c.LastName.label('last_name'),
                Player.c.FirstName.label('first_name'),
                Player.c.Birthday.label('birth_date'),
                Player.c.Gender.label('gender'),
                Player.c.EMail.label('email'),
                Address.c.Address1A.label('address_a'),
                Address.c.Address1B.label('address_b'),
                Address.c.City1.label('city'),
                Address.c.State1.label('state'),
                Address.c.Zip1.label('zip_code'),
                Address.c.Country1_ID.label('country'),
                Address.c.HomePhone1.label('phone'),
                Player.c.CallFlag.label('call_flag'),
                Player.c.MailFlag.label('mail_flag'),
                ])
    
    s = s.select_from(Player.join(Address, 
                          Player.c.Player_ID == Address.c.Player_ID))
    if player_id:
        s = s.where(Player.c.Player_ID == player_id)
    else:
        s = s.where(cast(Player.c.Timestamp, Date) == audit_date)
        
    try:                 
        rp = connection.execute(s)
        resultset = [dict(row) for row in rp]
        return resultset
        
    except Exception, e:
            extract_logger.info("Error extracting player data for %s" % audit_date)
            extract_logger.exception(e)
            
def employee_extract():
    s = select([Employee.c.User_ID.label('employee_id'),
                Employee.c.UserName.label('user_name'),
                Employee.c.FirstName.label('first_name'),
                Employee.c.LastName.label('last_name'),
                Employee.c.Title.label('title'),
                
                ])
    
    s = s.select_from(Employee)
        
    try:                 
        rp = connection.execute(s)
        resultset = [dict(row) for row in rp]
        return resultset
        
    except Exception, e:
            extract_logger.exception(e)

def group_extract(activity_date, player_id):
    s = select([Group.c.Group_ID.label('group_id'),
                Group.c.GroupName.label('group_name'),
                ])
    
    s = s.select_from(Group.join(GroupEnroll, 
                          Group.c.Group_ID == GroupEnroll.c.Group_ID))
    s = s.where(and_(GroupEnroll.c.Player_ID == player_id,
                     GroupEnroll.c.StartDateTime  <= activity_date,
                     GroupEnroll.c.EndDateTime  >= activity_date))
        
    try:                 
        rp = connection.execute(s)
        resultset = [dict(row) for row in rp]
        return resultset
        
    except Exception, e:
            extract_logger.info("Error extracting player data for %s" % activity_date)
            extract_logger.exception(e)

def slot_data_extract(audit_date, machine_num=None):
    extract_logger.info("Extracting slot records for %s" % audit_date )
    #fix for decimal problem
    for column in SlotMast.columns.values():
        if isinstance(column.type, Numeric):
            column.type.asdecimal = False

    s = select([SlotMast.c.SlotNumber.label('slot_number'),
                (SlotMast.c.CasinoCode).label('casino'),
                (SlotMast.c.Area).label('area'),
                (SlotMast.c.Section).label('section'),
                (SlotMast.c.Loc).label('position'),
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
                 
    s = s.select_from(SlotMast.join(RevisionHistory, and_(
                                       SlotMast.c.SlotMast_ID == RevisionHistory.c.SlotMast_ID,
                                       SlotMast.c.Revision == RevisionHistory.c.Revision,
                                       RevisionHistory.c.AuditDate == audit_date,
                                       ))\
                             .outerjoin(SlotType,  SlotMast.c.SlotType_ID == SlotType.c.SlotType_ID,)\
                             .outerjoin(Style, SlotMast.c.Style_ID == Style.c.Style_ID)\
                             .outerjoin(Mfr, SlotType.c.Mfr_ID == Mfr.c.Mfr_ID)\
                             .outerjoin(Cabinet, SlotMast.c.Cabinet_ID == Cabinet.c.Cabinet_ID)\
                             )             
    if machine_num:
        s = s.where(and_(RevisionHistory.c.AuditDate == audit_date, 
                         SlotMast.c.SlotNumber == machine_num))
    else:
        s = s.where(RevisionHistory.c.AuditDate == audit_date)
    s = s.distinct()                 
    
    try:                 
        rp = connection.execute(s)
        resultset = [dict(row) for row in rp]
        extract_logger.info("Extract successful")
        return resultset
        
    except Exception, e:
            extract_logger.info("Error extracting slot data for %s" % audit_date)
            extract_logger.exception(e)

def slot_revenue_extract(audit_date):
    #extract_logger.info("Extracting slot revenue records for %s" % audit_date )
    s = select([SlotMast.c.SlotNumber,
                SlotMast.c.CasinoCode,
                SlotMast.c.Area,
                SlotMast.c.Section,
                SlotMast.c.Loc,
                SlotMast.c.Lease_ID,
                SlotMast.c.ProgPC,
                Revenue,
                RevenuePBT.c.PtsCashDownElec,
                RevenuePBT.c.PromoDownMan
                ])
                      
    s = s.select_from(Revenue.join(RevisionHistory,
                 and_(
                      Revenue.c.SlotMast_ID == RevisionHistory.c.SlotMast_ID,
                      Revenue.c.AuditDate == RevisionHistory.c.AuditDate,
                      ))\
                 .join(SlotMast, 
                       and_(
                           RevisionHistory.c.SlotMast_ID == SlotMast.c.SlotMast_ID,
                           RevisionHistory.c.Revision == SlotMast.c.Revision,
                           ))\
                 .join(RevenuePBT, 
                       and_(
                           RevisionHistory.c.SlotMast_ID == RevenuePBT.c.SlotMast_ID,
                           RevenuePBT.c.AuditDate == Revenue.c.AuditDate,
                           RevenuePBT.c.Period_ID == Revenue.c.Period_ID,
                           )))
                   
    s = s.where(and_(Revenue.c.AuditDate == audit_date, 
                     Revenue.c.Period_ID == 4,
                     Revenue.c.DaysOnLine == 1))
    s = s.distinct()
    
    try:                 
        rp = connection.execute(s)
        resultset = [dict(row) for row in rp]
        extract_logger.info("Extract successful")
        return resultset
        
    except Exception, e:
            extract_logger.info("Error extracting slot revenue data for %s" % audit_date)
            extract_logger.exception(e)

def player_group_extract(audit_date, player_id=None):
    s = select([Group.c.GroupName.label('group_name'),
                Group.c.Group_ID.label('group_id'),
                ])
    
    s = s.select_from(Group.join(GroupEnroll, 
                          Group.c.Group_ID == GroupEnroll.c.Group_ID))
    s = s.where(and_(GroupEnroll.c.Player_ID == player_id,
                     GroupEnroll.c.StartDateTime <= audit_date,
                     GroupEnroll.c.EndDateTime >= audit_date
                     ))
        
    try:                 
        rp = connection.execute(s)
        resultset = [dict(row) for row in rp]
        return resultset
        
    except Exception, e:
            extract_logger.info("Error extracting player data for %s" % audit_date)
            extract_logger.exception(e)


def pit_revenue_extract(audit_date):
    #extract_logger.info("Extracting player session records for %s" %audit_date )
    s = select([TableDrop.c.Drop_ID.label('drop_id'),
                TableDrop.c.GamingDate.label('gaming_date'),
                TableDrop.c.Shift_ID.label('shift_id'),
                TableDrop.c.Location_ID.label('location_id'),
                cast(TableDrop.c.Cash1, Float).label('num_one_dollar'),
                cast(TableDrop.c.Cash2, Float).label('num_two_dollar'),
                cast(TableDrop.c.Cash5, Float).label('num_five_dollar'),
                cast(TableDrop.c.Cash10, Float).label('num_ten_dollar'),
                cast(TableDrop.c.Cash20, Float).label('num_twenty_dollar'),
                cast(TableDrop.c.Cash50, Float).label('num_fifty_dollar'),
                cast(TableDrop.c.Cash100, Float).label('num_hundred_dollar'),
                cast(TableDrop.c.Cash1000, Float).label('num_thousand_dollar'),
                cast(TableDrop.c.Other, Float).label('other'),
                cast(TableDrop.c.TotalCash, Float).label('total_cash'),
                cast(TableDrop.c.TotalChips, Float).label('total_chips'),
                cast(TableRevenue.c.OpenerChips, Float).label('open_chips'),
                cast(TableRevenue.c.CloseChips, Float).label('close_chips'),
                cast(TableRevenue.c.Fills, Float).label('fills'),
                cast(TableRevenue.c.StatisticalDrop, Float).label('stat_drop'),
                cast(TableRevenue.c.StatisticalWin, Float).label('stat_win'),
                
                ])
    
    s = s.select_from(TableDrop.join(TableRevenue, 
                          and_(TableDrop.c.GamingDate == TableRevenue.c.AuditDate,
                               TableDrop.c.Location_ID == TableRevenue.c.Location_ID,
                               TableDrop.c.Shift_ID == TableRevenue.c.Shift_ID)))
    
    s = s.where(TableDrop.c.GamingDate == audit_date)
                     
    #try:                 
    rp = connection.execute(s)
    resultset = [dict(row) for row in rp]
    extract_logger.info("Extract successful")
    return resultset
        
    #except Exception, e:
    #        extract_logger.info("Error extracting player session data for %s" %audit_date)
    #        extract_logger.error(e, exec_info=True)

def headcount_extract(audit_date):
    #extract_logger.info("Extracting player session records for %s" %audit_date )
    s = select([
            Headcount.c.iReportDataID.label('headcount_id'),
            Headcount.c.dtTime.label('date_time'),
            Headcount.c.iHour.label('hour'),
            Headcount.c.iMinute.label('minute'),
            cast(Headcount.c.mDenomination, Float).label('denomination'),
            Headcount.c.iGamesInPlay.label('games_in_play'),
            cast(Headcount.c.mCoinIn, Float).label('coin_in'),
            cast(Headcount.c.mCoinOut, Float).label('coin_out'),
            Headcount.c.iGamesStarts.label('handle_pulls'),
            Headcount.c.iTotalSlots.label('games_available'),
            Headcount.c.iCardedPlay.label('carded_play'),
            Headcount.c.iNonCardedPlay.label('noncarded_play'),
            Headcount.c.iTicketsIn.label('num_tickets_in'),
            Headcount.c.iTicketsOut.label('num_tickets_out'),
            Headcount.c.iJackpots.label('num_jackpots'),
            Headcount.c.iFills.label('num_fills'),
            Headcount.c.iPBTIn.label('num_pbt_in'),
            Headcount.c.iPBTOut.label('num_pbt_out'),
            Headcount.c.cCasinoCode.label('casino_code'),
            cast(Headcount.c.mPBTCashDownload, Float).label('amt_pbt_cash_downloaded'),
            cast(Headcount.c.mPBTPromoDownload, Float).label('amt_pbt_promo_downloaded'),
            cast(Headcount.c.mPBTRedeemCash, Float).label('amt_cash_redeemed'),
            cast(Headcount.c.mPBTRedeemPromo, Float).label('amt_promo_redeemed'),
            cast(Headcount.c.mPBTCashUpload, Float).label('amt_cash_uploaded'),
            cast(Headcount.c.mPBTCEPCreditsOut, Float).label('amt_cep_credits_out'),
        ])
    
    s = s.select_from(Headcount)
    
    s = s.where(cast(Headcount.c.dtTime, Date) == audit_date)
                     
    #try:                 
    rp = connection.execute(s)
    resultset = [dict(row) for row in rp]
    extract_logger.info("Extract successful")
    return resultset
        
    #except Exception, e:
    #        extract_logger.info("Error extracting player session data for %s" %audit_date)
    #        extract_logger.error(e, exec_info=True)

def player_stats_extract(end, days):
    end_date = parse(end)
    start_date = end_date - datetime.timedelta(days=days)
    s = select([Trip.c.Meta_ID.label('player_id'),
                functions.count(Trip.c.StatTrip_ID).label('trip_frequency'),
                functions.sum(TripDetail.c.CashIn).label('coin_in'),
                functions.sum(TripDetail.c.TWin).label('yield_theo'),
                functions.sum((TripDetail.c.CashIn
                 + TripDetail.c.ChipsIn
                 + TripDetail.c.MoneyPlay
                 + TripDetail.c.CreditIn
                 - TripDetail.c.JackPot
                 - TripDetail.c.CashOut)).label('yield_actual'),
                functions.sum(TripDetail.c.TimePlayed / 60.0).label('time_played'),
                functions.sum(TripDetail.c.PromoPlay).label('freeplay_used'),
                
                (functions.sum(TripDetail.c.TWin) / 
                    functions.count(Trip.c.StatTrip_ID)).label('adt'),
                
                (functions.sum(TripDetail.c.CashIn) / 
                    functions.count(Trip.c.StatTrip_ID)).label('average_daily_coin_in'),
                
                (functions.sum(TripDetail.c.PromoPlay) / 
                    functions.count(Trip.c.StatTrip_ID)).label('average_daily_freeplay_used'),
                
                (functions.sum(TripDetail.c.TimePlayed / 60.0) / 
                    functions.count(Trip.c.StatTrip_ID)).label('average_daily_time_played'),
                
                case([(functions.sum(TripDetail.c.PromoPlay) > 0, 
                       functions.sum(TripDetail.c.TWin) / 
                       functions.sum(TripDetail.c.PromoPlay))], 
                       else_= 0).label('freeplay_to_theo_win_ratio')])                
                
    
    s = s.select_from(Trip.join(TripDetail, 
                                Trip.c.StatTrip_ID == TripDetail.c.StatTrip_ID))
                                      
    s = s.where(and_(
        Trip.c.StartGamingDate.between(start_date, end_date),
        Trip.c.IDType == 'P',
        TripDetail.c.StatType == 'SLOT'))
        
    s = s.group_by(Trip.c.Meta_ID)
        
    rp = connection.execute(s)
    
    resultset = [dict(row) for row in rp]
    
    return resultset
    
def player_clv_data(end, days):
    end_date = parse(end)
    start_date = end_date - datetime.timedelta(days=days)
    s = select([Trip.c.Meta_ID.label('player_id'),
                Trip.c.StartGamingDate.label('start_date'),
                TripDetail.c.TWin.label('theo_win')])
    
    s = s.select_from(Trip.join(TripDetail, 
                                Trip.c.StatTrip_ID == TripDetail.c.StatTrip_ID))
                                      
    s = s.where(and_(
        Trip.c.StartGamingDate.between(start_date, end_date),
        Trip.c.IDType == 'P',
        TripDetail.c.StatType == 'SLOT'))
        
    s = s.group_by(Trip.c.Meta_ID, Trip.c.StartGamingDate, TripDetail.c.TWin)
        
    rp = connection.execute(s)
    
    resultset = [dict(row) for row in rp]
    
    return resultset
# -*- coding: utf-8 -*-
"""
Created on Thu Aug 04 16:56:39 2016

@author: Lathropk
"""
import datetime
import cdecimal
import pandas
import numpy as np
from lifetimes import BetaGeoFitter, GammaGammaFitter
from lifetimes.utils import summary_data_from_transaction_data
from dateutil.parser import parse
from django.db.models import Q
from django.conf import settings
from sqlalchemy import MetaData, select
from sqlalchemy.sql import and_
from conformed_dimensions.models import PitGameDimension, ShiftDimension,\
                                        PlayerDimension
from zip_codes.models import ZipCode
from oasis_utils.player_data import get_player

oasis_engine = settings.OASIS_ENGINE
metadata = MetaData(bind=oasis_engine)
metadata.reflect(only=['PlayerRankHistory',
                       'TieredRank',
                       'PB_Location'
                       ])
connection = oasis_engine.connect()

RankHistory = metadata.tables['PlayerRankHistory']
TieredRank = metadata.tables['TieredRank']
PitGame = metadata.tables['PB_Location']


def get_player_rec(rec):
    p_id = rec['player_id']
    if 'start_date' in rec:
        start = datetime.datetime.combine(rec['start_date'], datetime.time.max)
    elif 'start_time' in rec:
        start = rec['start_time']
    p = PlayerDimension.objects.filter(player_id = p_id,
                                       effective_date__lte = start)
    p = p.filter(Q(expiration_date__gte=start) | Q(expiration_date = None))
    if len(p) > 0:
        return p[0]
    else:
        rec_list = get_player(rec['player_id'])
        p_rec = rec_list[0]
        timestamp = p_rec['player_timestamp']
        try:
            city_state = p_rec['city'] + '_' + p_rec['state']
        except:
            city_state = None
            
        try:
            zipcode_obj = ZipCode.objects.filter(zip_code=p_rec['zip_code'][:5])[0]
            distance = zipcode_obj.distance
            lat = zipcode_obj.lat
            lon = zipcode_obj.lon
        except:
            distance = None
            lat = None
            lon = None
        p_rec.pop('player_timestamp', None)
        player = PlayerDimension(effective_date = timestamp,
                                     current = True,
                                     city_state = city_state,
                                     distance = distance,
                                     addr_lat = lat,
                                     addr_lon = lon,
                                     **p_rec)
        player.save()
        return player
    
    

def get_location_rec(location_id):
    try:
        s = select([PitGame.c.Location_ID.label('location_id'),
                    PitGame.c.Name.label('name'),
                    PitGame.c.ParentLocation_ID.label('parent_location')
                    ])
        
        s = s.select_from(PitGame)
        
        s = s.where(PitGame.c.Location_ID == location_id)
                         
                         
        rp = connection.execute(s)
        resultset = [dict(row) for row in rp]
        
        return resultset[0]
    except:
        return None
        
def get_shift_rec(shift_id):
    if shift_id == 'G':
        shift_dim = ShiftDimension.objects.get(shift='Grave')
    elif shift_id == 'D':
        shift_dim = ShiftDimension.objects.get(shift='Day')
    elif shift_id == 'S':
        shift_dim = ShiftDimension.objects.get(shift='Swing')
    else:
        shift_dim=None
    return shift_dim
                

def get_pit_game(location_id):
    try:
        pit_game_rec_1 = get_location_rec(location_id)
        pit_game_rec_2 = get_location_rec(pit_game_rec_1['parent_location'])
        pit_game_rec_3 = get_location_rec(pit_game_rec_2['parent_location'])
        
        game = pit_game_rec_1['name']
        game_type = pit_game_rec_2['name']
        pit = pit_game_rec_3['name']
        
        pitgame, created = PitGameDimension.objects.get_or_create(
                                oasis_id = location_id,
                                game = game.strip(),
                                game_type = game_type.strip(),
                                pit = pit.strip())
        return pitgame
    except:
        return None

def calculate_age(audit_date, born):
    if isinstance(audit_date, pandas.tslib.Timestamp):
        audit_date = audit_date.date()
    elif isinstance(audit_date, str):
        audit_date = parse(audit_date).date()
    elif isinstance(audit_date, datetime.datetime):
        audit_date = audit_date.date()
    
    try: 
        birthday = born.replace(year=audit_date.year)
    except ValueError: # raised when birth date is February 29 and the current year is not a leap year
        birthday = born.replace(year=audit_date.year, day=born.day-1)
    if birthday > audit_date:
        return audit_date.year - born.year - 1
    else:
        return audit_date.year - born.year

def create_geo_point(player):

    try:
        geo_point={}
        geo_point['lat'] = float(player.addr_lat)
        geo_point['lon'] = float(player.addr_lon)
        
    except:
        geo_point=None
    
    return geo_point

def get_player_tier(audit_date, player_id):
    s = select([RankHistory.c.RankID.label('rank_id'),
                RankHistory.c.PlayerID.label('player_id'),
                RankHistory.c.InsertedDatetime.label('inserted_date'),
                RankHistory.c.PriorHistoryID.label('prior_id'),
                TieredRank.c.Label.label('rank')
                ])
    
    s = s.select_from(RankHistory.join(TieredRank, 
                                    RankHistory.c.RankID == TieredRank.c.RankID))
    
    s = s.where(and_(RankHistory.c.PlayerID == player_id,
                     RankHistory.c.InsertedDatetime  < audit_date))
                     
    s = s.order_by(RankHistory.c.InsertedDatetime.desc())
                     
    rp = connection.execute(s)
    resultset = [dict(row) for row in rp]
    
    if resultset:
        return resultset[0]['rank']
    else:
        return None

def calc_clv(clv_recs, end, months=12):
    df = pandas.DataFrame(clv_recs)
    df = df[['player_id', 'start_date', 'theo_win']]
    df['theo_win'] = df['theo_win'].astype(float)
    
    end_date = parse(end)
    summary = summary_data_from_transaction_data(df, 
                                                 'player_id', 
                                                 'start_date', 
                                                 monetary_value_col='theo_win', 
                                                 observation_period_end=end_date)
    bgf = BetaGeoFitter(penalizer_coef=0.0)
    bgf.fit(summary['frequency'], summary['recency'], summary['T'])
    
    ggf = GammaGammaFitter(penalizer_coef = 0)
    ggf.fit(summary['frequency'], summary['monetary_value'])
    
    ggf_clv = ggf.customer_lifetime_value(
        bgf, #the model to use to predict the number of future transactions
        summary['frequency'],
        summary['recency'],
        summary['T'],
        summary['monetary_value'],
        time=months, 
        discount_rate=0.0
    )
    clv_df = pandas.DataFrame(ggf_clv)
    clv_df=clv_df.dropna()
    clv_df[clv_df['clv']<0] = 0.0
    summary=summary.merge(clv_df, left_index=True, right_index=True, how='inner')

    return summary

def clean_stat_dict_values(input_dict):
    for key, value in input_dict.items():
        if isinstance(value, cdecimal.Decimal):
            input_dict[key] = float(value)
        elif isinstance(value, float):
            if np.isnan(value):
                input_dict[key] = None
    
    return input_dict
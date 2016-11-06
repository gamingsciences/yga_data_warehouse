# -*- coding: utf-8 -*-
"""
Created on Tue Aug 02 11:11:15 2016

@author: Lathropk
"""
import pandas as pd
from django.db.models import Q
from dateutil.parser import parse
from preserialize.serialize import serialize
from conformed_dimensions.models import DateDimension, TimeDimension,\
                                        SlotGameDimension, EmployeeDimension
from utils.location_finder import get_location
from utils.loggers import TransformLogger
from utils.timezone_utils import local_to_utc
from zip_codes.models import ZipCode
from elastic.oasis_extract import group_extract
from utils.slot_revenue_utils import calc_gross_drop, calc_lease_fee,\
                                     calc_att_payouts_and_vouchers
from utils.transform_utils import create_geo_point, calculate_age, get_player_tier,\
                                  get_pit_game, get_player_rec, calc_clv, \
                                  clean_stat_dict_values


logger = TransformLogger()
transform_logger = logger.myLogger()


def transform_slot_sessions(audit_date, sessions):
    transform_logger.info("Updating Slot Player session records for %s" % audit_date )
    session_list = []
    for rec in sessions:
        #get dimension keys
        try:
            #Extract
            player = get_player_rec(rec)
            player_age = calculate_age(audit_date, player.birth_date)
            full_name = player.first_name + " " + player.last_name
            player_tier = get_player_tier(audit_date, player.player_id)
            
            sg = SlotGameDimension.objects.filter(slot_number = rec['slot_number'],
                                                   effective_date__lte = rec['start_time'])
            sg = sg.filter(Q(expiration_date__gte=rec['start_time']) | Q(expiration_date = None))
            slotgame = sg[0]
            
            location = get_location(rec)
             
            actual_win = rec['cash_in'] + rec['freeplay'] - rec['cash_out'] - rec['jackpots']
            date_dim = DateDimension.objects.get(full_date=rec['gaming_date'])
            #convert dates to UTC
            date_dim.full_date = local_to_utc(date_dim.full_date)
            date_dim.week_begin_date = local_to_utc(date_dim.week_begin_date)
            
            start_time = rec['start_time']
            num_minutes = start_time.hour*60 + start_time.minute
            time_dim = TimeDimension.objects.get(minute_of_day=num_minutes)
            
            #geo_point for player
            geo_point = create_geo_point(player)
            
            player_s = serialize(player)
            # clean up field the user does not need to see
            player_s.pop('effective_date', None)
            player_s.pop('expiration_date', None)
            player_s.pop('addr_lon', None)
            player_s.pop('addr_lat', None)
            player_s.pop('current', None)
            
            player_s['home_geo_point'] = serialize(geo_point)
            player_s['age'] = player_age
            player_s['full_name'] = full_name
            player_s['grc_rank'] = player_tier
            
            #get groups
            group_names = []
            group_ids = []
            groups = group_extract(audit_date, player.player_id)
            if groups:
                for group in groups:
                    group_names.append(group['group_name'])
                    group_ids.append(group['group_id'])
                     
            group_names_s = serialize(group_names)
            group_ids_s = serialize(group_ids)
            
            slotgame_s = serialize(slotgame)
            # clean up field the user does not need to see
            slotgame_s.pop('effective_date', None)
            slotgame_s.pop('expiration_date', None)
            slotgame_s.pop('current', None)
            
            slotgame_s['tags'] = list(slotgame.tags.names())
            location_s = serialize(location)
            date_s = serialize(date_dim)
            time_s = serialize(time_dim)
            
            rec['actual_win']=actual_win
            rec['player']=player_s
            rec['slotgame']=slotgame_s
            rec['location']=location_s
            rec['gaming_date']=date_s
            rec['time']=time_s
            rec['minutes_played']=rec['time_played']/60
            rec['group_names']=group_names_s
            rec['group_ids']=group_ids_s
            rec.pop('CasinoCode', None)            
            rec.pop('Area', None)            
            rec.pop('Section', None)            
            rec.pop('Loc', None)            
            rec.pop('player_id', None)            
            rec.pop('slot_number', None)            
            rec.pop('game', None)            
            rec.pop('pit', None)    
            rec.pop('time_played', None)
            
            session_list.append(rec)
            
        except Exception, e:
            transform_logger.info("Error processing: %s" % rec['session_id'])
            transform_logger.exception(e)
    
    transform_logger.info("Transform complete")       
    return session_list
    
def transform_pit_sessions(audit_date, sessions):
    transform_logger.info("Updating Pit Player session records for %s" % audit_date )
    session_list = []
    for rec in sessions:
        #get dimension keys
        try:
            #Extract
            player = get_player_rec(rec)
            player_age = calculate_age(audit_date, player.birth_date)
            full_name = player.first_name + " " + player.last_name
            player_tier = get_player_tier(audit_date, player.player_id)
            
            pit_game = get_pit_game(rec['pit'])
            rated_by = EmployeeDimension.objects.get(employee_id=rec['rated_by'])            
            
            actual_win = rec['cash_in'] + rec['chips_in'] + rec['freeplay'] - rec['cash_out'] - rec['jackpots']
            date_dim = DateDimension.objects.get(full_date=rec['gaming_date'])
            #convert dates to UTC
            date_dim.full_date = local_to_utc(date_dim.full_date)
            date_dim.week_begin_date = local_to_utc(date_dim.week_begin_date)
            
            start_time = rec['start_time']
            num_minutes = start_time.hour*60 + start_time.minute
            time_dim = TimeDimension.objects.get(minute_of_day=num_minutes)
            
            #geo_point for player
            geo_point = create_geo_point(player)
            
            player_s = serialize(player)
            # clean up field the user does not need to see
            player_s.pop('effective_date', None)
            player_s.pop('expiration_date', None)
            player_s.pop('current', None)
            player_s.pop('addr_lon', None)
            player_s.pop('addr_lat', None)
            
            player_s['home_geo_point'] = serialize(geo_point)
            player_s['age'] = player_age
            player_s['full_name'] = full_name
            player_s['grc_rank'] = player_tier
            
            #get groups
            group_names = []
            group_ids = []
            groups = group_extract(audit_date, player.player_id)
            if groups:
                for group in groups:
                    group_names.append(group['group_name'])
                    group_ids.append(group['group_id'])
                     
            group_names_s = serialize(group_names)
            group_ids_s = serialize(group_ids)
            
            pitgame_s = serialize(pit_game)
            
            date_s = serialize(date_dim)
            time_s = serialize(time_dim)
            
            rec['actual_win']=actual_win
            rec['player']=player_s
            rec['pitgame']=pitgame_s
            rec['gaming_date']=date_s
            rec['time']=time_s
            rec['minutes_played']=rec['time_played']/60
            rec['rated_by']=rated_by
            rec['group_names']=group_names_s
            rec['group_ids']=group_ids_s
            rec.pop('player_id', None)            
            rec.pop('slot_number', None)            
            rec.pop('game', None)            
            rec.pop('pit', None)     
            rec.pop('time_played', None)
            
            session_list.append(rec)
            
        except Exception, e:
            transform_logger.info("Error processing: %s" % rec['session_id'])
            transform_logger.exception(e)
    
    transform_logger.info("Transform complete")       
    return session_list

def transform_slot_trips(audit_date, trips):
    transform_logger.info("Updating Slot Player trip records for %s" % audit_date )
    trip_list = []
    for rec in trips:
        #get dimension keys
        try:
            #Extract
            player = get_player_rec(rec)
            
            player_age = calculate_age(audit_date, player.birth_date)
            full_name = player.first_name + " " + player.last_name
            player_tier = get_player_tier(audit_date, player.player_id)
            
            date_dim = DateDimension.objects.get(full_date=rec['start_date'])
            #convert dates to UTC
            date_dim.full_date = local_to_utc(date_dim.full_date)
            date_dim.week_begin_date = local_to_utc(date_dim.week_begin_date)
            rec['start_date']=local_to_utc(rec['start_date'])         
            rec['end_date']=local_to_utc(rec['end_date'])      
            
            actual_win = rec['cash_in'] + rec['freeplay'] - rec['cash_out'] - rec['jackpots']
            
            #get groups
            group_names = []
            group_ids = []
            groups = group_extract(audit_date, player.player_id)
            if groups:
                for group in groups:
                    group_names.append(group['group_name'])
                    group_ids.append(group['group_id'])
                     
            group_names_s = serialize(group_names)
            group_ids_s = serialize(group_ids)
            
            #geo_point for player
            geo_point = create_geo_point(player)
            
            player_s = serialize(player)
            # clean up field the user does not need to see
            player_s.pop('effective_date', None)
            player_s.pop('expiration_date', None)
            player_s.pop('current', None)
            player_s.pop('addr_lon', None)
            player_s.pop('addr_lat', None)
            
            player_s['home_geo_point'] = serialize(geo_point)
            player_s['age'] = player_age
            player_s['full_name'] = full_name
            player_s['grc_rank'] = player_tier
            
            rec['player']=player_s
            rec['gaming_date']=date_dim
            rec['minutes_played']=rec['time_played']/60
            rec['actual_win']=actual_win
            rec['group_names']=group_names_s
            rec['group_ids']=group_ids_s
            
            rec.pop('player_id', None)
            rec.pop('time_played', None)
            
            trip_list.append(rec)
            
        except Exception, e:
            transform_logger.info("Error processing: %d" % rec['trip_id'])
            transform_logger.exception(e)
    transform_logger.info("Transform complete")        
    return trip_list
    
def transform_pit_trips(audit_date, trips):
    transform_logger.info("Updating Pit Player trip records for %s" % audit_date )
    trip_list = []
    for rec in trips:
        #get dimension keys
        try:
            #Extract
            player = get_player_rec(rec)
            
            player_age = calculate_age(audit_date, player.birth_date)
            full_name = player.first_name + " " + player.last_name
            player_tier = get_player_tier(audit_date, player.player_id)
            
            date_dim = DateDimension.objects.get(full_date=rec['start_date'])
            #convert dates to UTC
            date_dim.full_date = local_to_utc(date_dim.full_date)
            date_dim.week_begin_date = local_to_utc(date_dim.week_begin_date)
            rec['start_date']=local_to_utc(rec['start_date'])         
            rec['end_date']=local_to_utc(rec['end_date'])      
            
            actual_win = rec['cash_in'] + rec['chips_in'] + rec['freeplay'] - rec['cash_out'] - rec['jackpots']
            
            #get groups
            group_names = []
            group_ids = []
            groups = group_extract(audit_date, player.player_id)
            if groups:
                for group in groups:
                    group_names.append(group['group_name'])
                    group_ids.append(group['group_id'])
                     
            group_names_s = serialize(group_names)
            group_ids_s = serialize(group_ids)
            
            #geo_point for player
            geo_point = create_geo_point(player)
            
            player_s = serialize(player)
            # clean up field the user does not need to see
            player_s.pop('effective_date', None)
            player_s.pop('expiration_date', None)
            player_s.pop('current', None)
            player_s.pop('addr_lon', None)
            player_s.pop('addr_lat', None)
            
            player_s['home_geo_point'] = serialize(geo_point)
            player_s['age'] = player_age
            player_s['full_name'] = full_name
            player_s['grc_rank'] = player_tier
            
            rec['player']=player_s
            rec['gaming_date']=date_dim
            rec['minutes_played']=rec['time_played']/60
            rec['actual_win']=actual_win
            rec['group_names']=group_names_s
            rec['group_ids']=group_ids_s
            
            rec.pop('player_id', None)
            rec.pop('time_played', None)
            
            trip_list.append(rec)
            
        except Exception, e:
            transform_logger.info("Error processing: %d" % rec['trip_id'])
            transform_logger.exception(e)
    transform_logger.info("Transform complete")        
    return trip_list

def transform_slot_revenue(audit_date, revenue_records):
    transform_logger.info("Updating slot revenue records for %s" % audit_date )
    revenue_recs =[]
    for rec in revenue_records:
        try:
            location = get_location(rec)
            location_s = serialize(location)
            
            # get the date object form the condormed_dim Date model        
            date_dim = DateDimension.objects.get(full_date=rec['AuditDate'])
            #convert dates to UTC
            date_dim.full_date = local_to_utc(date_dim.full_date)
            date_dim.week_begin_date = local_to_utc(date_dim.week_begin_date)
            
            sg = SlotGameDimension.objects.filter(slot_number = rec['SlotNumber'],
                                                       effective_date__lte = rec['AuditDate'])
            sg = sg.filter(Q(expiration_date__gte=rec['AuditDate']) | Q(expiration_date = None))
            slotgame = sg[0]
            slotgame_s = serialize(slotgame)
            # clean up field the user does not need to see
            slotgame_s.pop('effective_date', None)
            slotgame_s.pop('expiration_date', None)
            slotgame_s.pop('current', None)
            
            slotgame_s['tags'] = list(slotgame.tags.names())
            
            coin_in = float(rec['ElecCoinIn'])
            gross_drop = float(calc_gross_drop(rec))
            att_payouts_and_vouchers = float(calc_att_payouts_and_vouchers(rec))
            points_cashed_amt = float(rec['PtsCashDownElec'])
            net_win_taxable = gross_drop - att_payouts_and_vouchers + points_cashed_amt
            freeplay_amt = float(rec['PromoDownMan'])
            lease_fee = float(calc_lease_fee(rec))
            adj_net_win = net_win_taxable + freeplay_amt - lease_fee
            try:
                hold = adj_net_win / coin_in
            except:
                hold = None
                
            theo_win = float(rec['ElecCoinIn']) * (slotgame.par * 0.01)
            est_var = adj_net_win - theo_win
            try:
                avg_bet = float(rec['ElecCoinIn']) / float(rec['GameStart'])
            except:
                avg_bet = None
            try:
                hit_freq = float(rec['MeteredGamesWon']) / float(rec['GameStart'])
            except:
                hit_freq = None
            
            revenue_rec = {}
            revenue_rec['slot_number']=rec['SlotNumber']
            revenue_rec['coin_in']=coin_in
            revenue_rec['coin_out']=float(rec['ElecCoinOut'])
            revenue_rec['gross_drop']=gross_drop
            revenue_rec['att_payouts_and_vouchers']=att_payouts_and_vouchers
            revenue_rec['points_cashed_amt']=points_cashed_amt
            revenue_rec['net_win_taxable']=net_win_taxable
            revenue_rec['freeplay_amt']=freeplay_amt
            revenue_rec['adj_net_win']=adj_net_win
            revenue_rec['hold']=hold
            revenue_rec['theo_win']=theo_win
            revenue_rec['est_var']=est_var
            revenue_rec['lease_fee']=lease_fee
            revenue_rec['num_fifty_dollar']=rec['ManualFifties']
            revenue_rec['num_five_dollar']=rec['ManualFives']
            revenue_rec['num_hundred_dollar']=rec['ManualHundreds']
            revenue_rec['num_one_dollar']=rec['ManualOnes']
            revenue_rec['num_ten_dollar']=rec['ManualTens']
            revenue_rec['num_twenty_dollar']=rec['ManualTwenties']
            revenue_rec['num_two_dollar']=rec['ManualTwos']
            revenue_rec['bills_in_amt']=float(rec['ActualBillIn'])
            revenue_rec['tickets_in_amt']=float(rec['ActualVoucherIn'])
            revenue_rec['tickets_out_amt']=float(rec['ElecTicketOut'])
            revenue_rec['handle_pulls']=rec['GameStart']
            revenue_rec['games_won']=rec['MeteredGamesWon']
            revenue_rec['hit_freq']=hit_freq
            revenue_rec['avg_bet']=avg_bet
            revenue_rec['jackpots']=float(rec['Jackpots'])
            revenue_rec['machine_paid_prog']=float(rec['MeteredMachPaidProg'])
            
            revenue_rec['gaming_date']=date_dim
            
            revenue_rec['location']=location_s
            
            revenue_rec['slotgame']=slotgame_s
            
            
            revenue_recs.append(revenue_rec)
        except Exception, e:
            transform_logger.exception(e)
            
    transform_logger.info("Transform complete")
    return revenue_recs

def transform_pit_revenue(audit_date, revenue_records):
    transform_logger.info("Updating pit revenue records for %s" % audit_date )
    recs =[]
    for rec in revenue_records:
        try:
            # get the date object form the condormed_dim Date model        
            date_dim = DateDimension.objects.get(full_date=rec['gaming_date'])
            #convert dates to UTC
            date_dim.full_date = local_to_utc(date_dim.full_date)
            date_dim.week_begin_date = local_to_utc(date_dim.week_begin_date)
            
            #get pit game
            pit_game = get_pit_game(rec['location_id'])
            
            rec['gaming_date'] = date_dim
            rec['game'] = pit_game
            
            recs.append(rec)
        except Exception, e:
            transform_logger.info("Error processing: %d" % rec['trip_id'])
            transform_logger.exception(e)
    transform_logger.info("Transform complete")
    return recs

def transform_slot_data(audit_date, slot_records):
    transform_logger.info("Updating slot data records for %s" % audit_date )
    slot_recs =[]
    for rec in slot_records:
        location = get_location(rec)
        location_s = serialize(location)
        
        # get the date object form the conformed_dim Date model        
        date_dim = DateDimension.objects.get(full_date=rec['edit_date'])
        #convert dates to UTC
        date_dim.full_date = local_to_utc(date_dim.full_date)
        date_dim.week_begin_date = local_to_utc(date_dim.week_begin_date)
        date_s = serialize(date_dim)
        
        slot_rec = {}
        slot_rec['edit_date']=date_s
        
        slot_rec['location']=location_s
        
        slot_rec['slot_number']=rec['slot_number']
        slot_rec['cabinet']=rec['cabinet']
        slot_rec['denomination']=float(rec['denomination'])
        slot_rec['description']=rec['description']
        slot_rec['game_type']=rec['game_type']
        slot_rec['manufacturer']=rec['manufacturer']
        slot_rec['multidenom']=rec['multidenom']
        slot_rec['multigame']=rec['multigame']
        slot_rec['num_coins']=rec['num_coins']
        slot_rec['num_paylines']=rec['num_paylines']
        slot_rec['num_reels']=rec['num_reels']
        slot_rec['par']=rec['par']
        slot_rec['progressive']=rec['progressive']
        
        slot_recs.append(rec)        
    transform_logger.info("Transform complete")
    return slot_recs
    
def transform_player(rec):
    player_id = rec['player_id']
    transform_logger.info("Transforming player record %s" % player_id)
    #calculate and add player age, distance from casino, drivetime, marketing tier,
    # and location geo_point
    
    try:
        zip_code_obj = ZipCode.objects.filter(zip_code=rec['zip_code'][:5])[0]
    except:
        zip_code_obj = None
    if zip_code_obj:
        geo_point={}
        geo_point['lat'] = zip_code_obj.lat
        geo_point['lon'] = zip_code_obj.lon
        
    else:
        geo_point=None
    
    rec['geo_point'] = geo_point
    
    return rec

def transform_headcount(recs):
    #transform_logger.info("Transforming player record %s" % player_id)
    headcount_recs=[]
    for rec in recs:
        # get the date object form the conformed_dim Date model        
        date_dim = DateDimension.objects.get(full_date=rec['date_time'])
        #convert dates to UTC
        date_dim.full_date = local_to_utc(date_dim.full_date)
        rec['date_time']=local_to_utc(rec['date_time'])
        
        num_minutes = rec['hour']*60 + rec['minute']
        time_dim = TimeDimension.objects.get(minute_of_day=num_minutes)
        
        try:
            casino_str = str.strip(rec['casino_code'])
        except:
            casino_str = ''
        if casino_str == '10':
            casino_name = 'YC'
        else:
            casino_name = 'Buckys'    
        
        rec['gaming_date']=date_dim
        rec['time']=time_dim
        rec['casino']=casino_name
        rec.pop('hour', None)
        rec.pop('minute', None)
        rec.pop('casino_code', None)
        
        headcount_recs.append(rec)
    
    return headcount_recs
    
def transform_daily_budget(recs):
    budget_recs =[]
    for rec in recs:
        date_dim = DateDimension.objects.get(full_date=rec['budget_date'])
        #convert dates to UTC
        date_dim.full_date = local_to_utc(date_dim.full_date)
        
        rec['gaming_date']=date_dim
        rec['location']={'casino':rec['casino']}
        rec.pop('budget_date', None)
        rec.pop('casino', None)
        budget_recs.append(rec)
    
    return budget_recs
    
def transform_player_stats(audit_date, stat_recs, clv_recs, 
                           stats_time='1 month', clv_time='12 month'):
    s_recs = []
    stat_df = pd.DataFrame.from_records(stat_recs, index='player_id')
    clv_summary = calc_clv(clv_recs, audit_date)
    combine_df = pd.concat([clv_summary, stat_df], axis=1)
    combine_dict = combine_df.to_dict(orient='index')
    player_ids = combine_dict.keys()
    for player_id in player_ids:
        try:
            rec = clean_stat_dict_values(combine_dict[player_id])
            rec['player_id'] = int(player_id)
            rec['start_date'] = parse(audit_date)
            date_dim = DateDimension.objects.get(full_date=rec['start_date'])
            #convert dates to UTC
            date_dim.full_date = local_to_utc(date_dim.full_date)
            date_dim.week_begin_date = local_to_utc(date_dim.week_begin_date)
            
            player = get_player_rec(rec)
            player_age = calculate_age(audit_date, player.birth_date)
            full_name = player.first_name + " " + player.last_name
            player_tier = get_player_tier(audit_date, player.player_id)
            
            #geo_point for player
            geo_point = create_geo_point(player)
            
            date_s = serialize(date_dim)
            
            player_s = serialize(player)
            # clean up field the user does not need to see
            player_s.pop('effective_date', None)
            player_s.pop('expiration_date', None)
            player_s.pop('addr_lon', None)
            player_s.pop('addr_lat', None)
            player_s.pop('current', None)
            
            player_s['home_geo_point'] = serialize(geo_point)
            player_s['age'] = player_age
            player_s['full_name'] = full_name
            player_s['grc_rank'] = player_tier
                
            rec['player']=player_s
            rec['gaming_date']=date_s
            rec['clv_T']=rec.pop('T')
            rec['clv_frequency']=rec.pop('frequency')
            rec['clv_monetary_value']=rec.pop('monetary_value')
            rec['clv_recency']=rec.pop('recency')
            rec['stats_timeframe']=stats_time
            rec['clv_timeframe']=clv_time
            rec.pop('player_id', None)
            rec.pop('start_date', None)
            
            
            s_recs.append(rec)
        except Exception, e:
                print e
    return s_recs

# -*- coding: utf-8 -*-
"""
Created on Mon Sep 26 10:40:22 2016

@author: Lathropk
"""
import datetime
import csv
import calendar
import holidays
import bisect
from geopy.distance import vincenty
from dateutil.parser import parse
from django.conf import settings
from oasis_utils.player_data import player_load
from oasis_utils.slot_data import game_load
from zip_codes.models import ZipCode
from conformed_dimensions.models import DateDimension, TimeDimension,\
                                        PlayerDimension, SlotGameDimension,\
                                        DailyBudgetDimension


def load_date_recs(start_date, num_days):
    date_obj = parse(start_date).date()
    
    for delta in range(num_days):
        create_date_rec(date_obj + datetime.timedelta(days=delta))
        
def load_time_recs():
    for t in range(0, 1441):
        time_str=str(datetime.timedelta(minutes=t)).split(':')
        hour=int(time_str[0])
        minute=time_str[1]
        if hour == 0:
            clock_time = '12'   + ':' + minute + ' AM'
        elif hour < 12:
            clock_time = str(hour) + ':' + minute + ' AM'
        elif hour == 12:
            clock_time = str(hour) + ':' + minute + ' PM'
        else:
            clock_time = str(hour - 12) + ':' + minute + ' PM'
        
        t_obj=TimeDimension(minute_of_day=t,
                            hour=hour,
                            minute=int(minute),
                            clock_time=clock_time)
        t_obj.save()

def create_date_rec(date_obj):
    day_info_dict = day_info()
    month_info_dict = month_info()
    dd_obj = DateDimension(datekey = int(date_obj.strftime('%Y%m%d')),
                           full_date = date_obj,
                           day_of_week = date_obj.weekday()+1,
                           day_num_in_month = date_obj.day,
                           day_name = day_info_dict[date_obj.weekday()][0],
                           day_abbrev = day_info_dict[date_obj.weekday()][1],
                           weekday_flag = day_info_dict[date_obj.weekday()][2],
                           week_num_in_year = date_obj.isocalendar()[1],
                           week_begin_date = get_start_of_week(date_obj)[0],
                           week_begin_datekey = get_start_of_week(date_obj)[1],
                           month = date_obj.month,
                           month_name = month_info_dict[date_obj.month][0],
                           month_abbrev = month_info_dict[date_obj.month][1],
                           quarter = calc_quarter(date_obj),
                           year = date_obj.year,
                           yearmo = int(date_obj.strftime('%Y%m')),
                           month_end_flag = test_month_end(date_obj),
                           holiday_flag = test_holiday(date_obj)
                           )
    dd_obj.save()

def load_players():
    player_recs = player_load()
    for rec in player_recs:
        print rec['player_id']
        try:
            city_state = rec['city'] + '_' + rec['state']
        except:
            city_state = None
            
        try:
            zip_obj = ZipCode.objects.filter(zip_code=rec['zip_code'][:5])[0]
            distance = zip_obj.distance
            lat = zip_obj.lat
            lon = zip_obj.lon
        except:
            distance = None
            lat = None
            lon = None
        
        effective_date = rec['date_joined']
       
        player = PlayerDimension(effective_date = effective_date,
                                     current = True,
                                     city_state = city_state,
                                     distance = distance,
                                     addr_lat = lat,
                                     addr_lon = lon,
                                     **rec)
        player.save()
        
        
def load_slot_games():
    game_recs = game_load()
    for rec in game_recs:
        print rec['slot_number']
        timestamp = rec['edit_date']
            
        # check for active game record
        previous_game_rec = SlotGameDimension.objects.filter(slot_number=rec['slot_number'],
                                                             current=True)
        if previous_game_rec.exists():
            g = previous_game_rec[0]
            if g.effective_date == timestamp:
                continue
            else:
                g.expiration_date = timestamp
                g.current=False
                g.save()
            
        effective_date = timestamp
        del rec['edit_date']
        
        game = SlotGameDimension(effective_date = effective_date,
                                     current = True,
                                     **rec)
        game.save()


def get_distance(lat, lon):
    casino=settings.CASINO_GEO_POINT
    player_loc=(lat, lon)
    return vincenty(casino, player_loc).miles
        
def load_zipcode_data(filename):
    with open(filename, 'rb')as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            code = ZipCode(zip_code = row[1],
                           state_abrev = row[2],
                           lat = row[3],
                           lon = row[4],
                           city = row[5],
                           state = row[6],
                           distance = get_distance(row[3], row[4]))
            code.save()
            
def load_budget_data(filename):
    with open(filename, 'rb')as csvfile:
        reader = csv.reader(csvfile)
        reader.next()
        for row in reader:
            date_ = parse(row[0]).date()
            obj = DailyBudgetDimension(budget_date = date_,
                                        casino = row[1],
                                        previous_year_slot_win = row[2],
                                        budget_slot_win = row[3],
                                        budget_coin_in = row[4],
                                        budget_table_win = row[5],
                                        budget_f_and_b_revenue = row[6])
            obj.save()
    
#-------------------------Date Dim Utilites-------------------------------------
def get_start_of_week(date_obj):
    day_of_week = date_obj.weekday()
    
    to_start_of_week = datetime.timedelta(days=day_of_week)
    
    week_start = date_obj - to_start_of_week
    week_start_key = int(date_obj.strftime('%Y%m%d'))
    
    return [week_start, week_start_key]

def day_info():
    day_info_dict = {6:['Sunday', 'Sun', False],
                     0:['Monday', 'Mon', True],
                     1:['Tuesday', 'Tue', True],
                     2:['Wednesday', 'Wed', True],
                     3:['Thursday', 'Thu', True],
                     4:['Friday', 'Fri', True],
                     5:['Saturday', 'Sat', False]
                     }
    return day_info_dict

def month_info():
    month_info_dict = {1:['January', 'Jan'],
                       2:['February', 'Feb'],
                       3:['March', 'Mar'],
                       4:['April', 'Apr'],
                       5:['May', 'May'],
                       6:['June', 'Jun'],
                       7:['July', 'Jul'],
                       8:['August', 'Aug'],
                       9:['September', 'Sep'],
                       10:['October', 'Oct'],
                       11:['November', 'Nov'],
                       12:['December', 'Dec']
                       }
    return month_info_dict

def calc_quarter(date_obj):
    quarters = range(1, 12, 3)
    month = date_obj.month
    quarter = bisect.bisect(quarters, month)
    qtr_str = 'Q' + str(quarter)
    
    return qtr_str
    
def test_month_end(date_obj):
    return calendar.monthrange(date_obj.year, date_obj.month)[1] == date_obj.day

def test_holiday(date_obj):
    us_holidays = holidays.US()
    return date_obj in us_holidays    
    
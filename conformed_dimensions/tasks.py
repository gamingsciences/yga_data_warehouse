# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:36:00 2016

@author: Lathropk
"""
from __future__ import absolute_import
from celery import shared_task
import datetime
import pandas as pd
from oasis_utils.player_data import player_update
from oasis_utils.slot_data import game_update
from elastic.oasis_extract import employee_extract
from .models import PlayerDimension, SlotGameDimension, EmployeeDimension
from zip_codes.models import ZipCode
from utils.loggers import UpdateDimLogger

logger = UpdateDimLogger()
update_logger = logger.myLogger()


@shared_task()
def update_player_recs():
    last_update = PlayerDimension.objects.all().latest('effective_date').effective_date
    start_date = last_update.date() + datetime.timedelta(days=1)
    today = datetime.datetime.now().date()
    end_date = today - datetime.timedelta(days=1)
    dates = pd.date_range(start_date, end_date).tolist()
    for date in dates:
        update_players(date)
    
def update_players(audit_date):
    update_logger.info("Updating Player records for %s" % audit_date )
    player_recs = player_update(audit_date)
    for rec in player_recs:
        update_player(rec)
    update_logger.info("Update complete")

def update_player(rec):
    timestamp = rec['player_timestamp']
    try:
        city_state = rec['city'] + '_' + rec['state']
    except:
        city_state = None
        
    try:
        zipcode_obj = ZipCode.objects.filter(zip_code=rec['zip_code'][:5])[0]
        distance = zipcode_obj.distance
        lat = zipcode_obj.lat
        lon = zipcode_obj.lon
    except:
        distance = None
        lat = None
        lon = None
        
    # check for active player record
    previous_player_rec = PlayerDimension.objects.filter(player_id=rec['player_id'],
                                                         current=True)
        
    if previous_player_rec.exists():
        p = previous_player_rec[0]
        p.expiration_date = timestamp
        p.current=False
        p.save()
        
        
    else:
        # if date joined is less than timestamp, create a previous record before
        # the update
        if rec['date_joined'].date() < rec['player_timestamp'].date():
            
            joined_date = rec['date_joined']
            rec.pop('player_timestamp', None)
            try:
                player = PlayerDimension(effective_date = joined_date,
                                         current = False,
                                         city_state = city_state,
                                         distance = distance,
                                         addr_lat = lat,
                                         addr_lon = lon,
                                         expiration_date = timestamp,
                                         **rec)
                player.save()
            except Exception, e:
                update_logger.info("Error processing: %s" % rec['player_id'])
                update_logger.exception(e)
        
        
    rec.pop('player_timestamp', None)
    try:
        player = PlayerDimension(effective_date = timestamp,
                                 current = True,
                                 city_state = city_state,
                                 distance = distance,
                                 addr_lat = lat,
                                 addr_lon = lon,
                                 **rec)
        player.save()
    except Exception, e:
        update_logger.info("Error processing: %s" % rec['player_id'])
        update_logger.exception(e)

@shared_task()
def update_employee_recs():
    employees = employee_extract()
    warehouse_employees = EmployeeDimension.objects.all()
    
    id_list = [rec['employee_id'] for rec in employees]
    warehouse_list = [rec.employee_id for rec in warehouse_employees]
    
    diff = list(set(id_list) - set(warehouse_list))
    
    for emp_id in diff:
        for rec in employees:
            if rec['employee_id'] == emp_id:
                employee = EmployeeDimension(**rec)
                employee.save()           

@shared_task()
def update_slot_game_recs():
    last_update = SlotGameDimension.objects.all().latest('effective_date').effective_date
    start_date = last_update.date() + datetime.timedelta(days=1)
    today = datetime.datetime.now().date()
    end_date = today - datetime.timedelta(days=1)
    dates = pd.date_range(start_date, end_date).tolist()
    for date in dates:
        update_slot_games(date)


def update_slot_games(audit_date):
    update_logger.info("Updating Slot records for %s" % audit_date )
    game_recs = game_update(audit_date)
    for rec in game_recs:
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
        
        try:
            game = SlotGameDimension(effective_date = effective_date,
                                     current = True,
                                     **rec)
            game.save()
        except Exception, e:
            update_logger.info("Error processing: %s" % rec['slot_number'])
            update_logger.exception(e)
    update_logger.info("Update complete")

def update_all():
    update_player_recs()
    update_employee_recs()
    update_slot_game_recs()
    
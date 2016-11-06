# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:17:55 2016

@author: Lathropk
"""
import datetime
from preserialize.serialize import serialize
from django.conf import settings
from oasis_extract import slot_session_extract, slot_trip_extract,\
                          pit_session_extract, pit_trip_extract, \
                          player_stats_extract, player_clv_data
from transform import transform_slot_sessions, transform_slot_trips,\
                      transform_pit_sessions, transform_pit_trips, \
                      transform_player_stats
from elasticsearch import Elasticsearch, helpers

es_host = settings.ES_HOST

def slot_sessions_etl(audit_date):
    es = Elasticsearch([es_host])
    batch_chunks = []
    iterator = 0
    sessions_ext = slot_session_extract(audit_date)
    sessions_trans = transform_slot_sessions(audit_date, sessions_ext)
    for session in sessions_trans:
        s = serialize(session)
        data_dict = {
                "_index": "slot_sessions", 
                "_type": "session",
                "_id": session['session_id'],
                "_source": s
        }
        
        batch_chunks.append(data_dict)
        if iterator % 100 == 0:
            helpers.bulk(es, batch_chunks, request_timeout=60)
            del batch_chunks[:]
        iterator = iterator + 1
    
    if len(batch_chunks) != 0:
        helpers.bulk(es, batch_chunks)

def pit_sessions_etl(audit_date):
    es = Elasticsearch([es_host])
    batch_chunks = []
    iterator = 0
    sessions_ext = pit_session_extract(audit_date)
    sessions_trans = transform_pit_sessions(audit_date, sessions_ext)
    for session in sessions_trans:
        s = serialize(session)
        data_dict = {
                "_index": "pit_sessions", 
                "_type": "session",
                "_id": session['session_id'],
                "_source": s
        }
        
        batch_chunks.append(data_dict)
        if iterator % 100 == 0:
            helpers.bulk(es, batch_chunks, request_timeout=60)
            del batch_chunks[:]
        iterator = iterator + 1
    
    if len(batch_chunks) != 0:
        helpers.bulk(es, batch_chunks)            

def slot_trips_etl(audit_date):
    es = Elasticsearch([es_host])
    batch_chunks = []
    iterator = 0
    trips_ext = slot_trip_extract(audit_date)
    trips_trans = transform_slot_trips(audit_date, trips_ext)
    for trip in trips_trans:
        s = serialize(trip)
        data_dict = {
                "_index": "slot_trips", 
                "_type": "trip",
                "_id": trip['trip_id'],
                "_source": s
        }
        
        batch_chunks.append(data_dict)
        if iterator % 100 == 0:
            helpers.bulk(es, batch_chunks, request_timeout=60)
            del batch_chunks[:]
        iterator = iterator + 1
    
    if len(batch_chunks) != 0:
        helpers.bulk(es, batch_chunks)

def pit_trips_etl(audit_date):
    es = Elasticsearch([es_host])
    batch_chunks = []
    iterator = 0
    trips_ext = pit_trip_extract(audit_date)
    trips_trans = transform_pit_trips(audit_date, trips_ext)
    for trip in trips_trans:
        s = serialize(trip)
        data_dict = {
                "_index": "pit_trips", 
                "_type": "trip",
                "_id": trip['trip_id'],
                "_source": s
        }
        
        batch_chunks.append(data_dict)
        if iterator % 100 == 0:
            helpers.bulk(es, batch_chunks, request_timeout=60)
            del batch_chunks[:]
        iterator = iterator + 1
    
    if len(batch_chunks) != 0:
        helpers.bulk(es, batch_chunks)
        
def player_stats_etl(audit_date):
    es = Elasticsearch([es_host])
    batch_chunks = []
    iterator = 0
    stats_ext = player_stats_extract(audit_date, 30) #30
    clv_data_ext = player_clv_data(audit_date, 360) #360
    stats_trans = transform_player_stats(audit_date, stats_ext, clv_data_ext)
    for rec in stats_trans:
        s = serialize(rec)
        data_dict = {
                "_index": "slot_player_stats", 
                "_type": "stats",
                "_id": str(s['player']['player_id']) + '_' + str(s['gaming_date']['datekey']),
                "_source": s
        }
        
        batch_chunks.append(data_dict)
        if iterator % 100 == 0:
            try:
                helpers.bulk(es, batch_chunks, request_timeout=60)
            except:
                pass
            del batch_chunks[:]
        iterator = iterator + 1
    
    if len(batch_chunks) != 0:
        helpers.bulk(es, batch_chunks)

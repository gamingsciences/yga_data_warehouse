# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 12:17:55 2016

@author: Lathropk
"""
from __future__ import absolute_import
from celery import shared_task
import datetime
import pandas as pd
from dateutil.parser import parse
from elastic.gaming_revenue_etl import slot_revenue_etl, pit_revenue_etl
from elastic.player_activity_etl import slot_sessions_etl, slot_trips_etl,\
                                        pit_sessions_etl, pit_trips_etl
from elastic.headcount_etl import headcount_etl
from utils.loggers import UpdateElasticLogger
from utils.timezone_utils import utc_to_local
from django.conf import settings

from elasticsearch import Elasticsearch

es_host = settings.ES_HOST

logger = UpdateElasticLogger()
elastic_logger = logger.myLogger()


#@shared_task
def update_slot_revenue_recs():
    elastic_logger.info("Updating elasticsearch Slot Revenue Documents" )
    try:
        es = Elasticsearch([es_host])
        query = {
            'query': {
                'match_all': {},
            },
            'sort': {
                    'gaming_date.full_date': {"order": "desc"}
            },
            'size': '1'
        }
        res = es.search(index='slot_revenue', body=query)
        
        d = res['hits']['hits'][0]['_source']['gaming_date']['full_date']
        last_update = utc_to_local(parse(d))
        start_date = last_update + datetime.timedelta(days=1)
        today = datetime.datetime.now().date()
        end_date = today - datetime.timedelta(days=1)
        if start_date == end_date:
            slot_revenue_etl(start_date)
        else:
            dates = pd.date_range(start_date, end_date).tolist()
            for date in dates:
                slot_revenue_etl(date)
    except Exception, e:
            elastic_logger.exception(e)
    elastic_logger.info("Update complete")

@shared_task
def update_slot_trip_recs():
    elastic_logger.info("Updating elasticsearch Slot Trip Documents" )
    try:
        es = Elasticsearch([es_host])
        query = {
            'query': {
                'match_all': {},
            },
            'sort': {
                    'gaming_date.full_date': {"order": "desc"}
            },
            'size': '1'
        }
        res = es.search(index='slot_trips', body=query)
        
        d = res['hits']['hits'][0]['_source']['gaming_date']['full_date']
        last_update = utc_to_local(parse(d)).date()
        start_date = last_update + datetime.timedelta(days=1)
        today = datetime.datetime.now().date()
        end_date = today - datetime.timedelta(days=1)
        if start_date == end_date:
            slot_trips_etl(start_date)
        else:
            dates = pd.date_range(start_date, end_date).tolist()
            for date in dates:
                slot_trips_etl(date)
    except Exception, e:
            elastic_logger.exception(e)
    elastic_logger.info("Update complete")

@shared_task
def update_slot_session_recs():
    elastic_logger.info("Updating elasticsearch Slot Session Documents" )
    try:
        es = Elasticsearch([es_host])
        query = {
            'query': {
                'match_all': {},
            },
            'sort': {
                    'gaming_date.full_date': {"order": "desc"}
            },
            'size': '1'
        }
        res = es.search(index='slot_sessions', body=query)
        
        d = res['hits']['hits'][0]['_source']['gaming_date']['full_date']
        last_update = utc_to_local(parse(d))
        start_date = last_update + datetime.timedelta(days=1)
        today = datetime.datetime.now().date()
        end_date = today - datetime.timedelta(days=1)
        if start_date == end_date:
            slot_sessions_etl(start_date)
        else:
            dates = pd.date_range(start_date, end_date).tolist()
            for date in dates:
                slot_sessions_etl(date)
    except Exception, e:
            elastic_logger.exception(e)
    elastic_logger.info("Update complete")

#@shared_task
def update_pit_revenue_recs():
    elastic_logger.info("Updating elasticsearch Pit Revenue Documents" )
    try:
        es = Elasticsearch([es_host])
        query = {
            'query': {
                'match_all': {},
            },
            'sort': {
                    'gaming_date.full_date': {"order": "desc"}
            },
            'size': '1'
        }
        res = es.search(index='pit_revenue', body=query)
        
        d = res['hits']['hits'][0]['_source']['gaming_date']['full_date']
        last_update = utc_to_local(parse(d))
        start_date = last_update + datetime.timedelta(days=1)
        today = datetime.datetime.now().date()
        end_date = today - datetime.timedelta(days=1)
        if start_date == end_date:
            pit_revenue_etl(start_date)
        else:
            dates = pd.date_range(start_date, end_date).tolist()
            for date in dates:
                pit_revenue_etl(date)
    except Exception, e:
            elastic_logger.exception(e)
    elastic_logger.info("Update complete")

@shared_task
def update_pit_trip_recs():
    elastic_logger.info("Updating elasticsearch Pit Trip Documents" )
    try:
        es = Elasticsearch([es_host])
        query = {
            'query': {
                'match_all': {},
            },
            'sort': {
                    'gaming_date.full_date': {"order": "desc"}
            },
            'size': '1'
        }
        res = es.search(index='pit_trips', body=query)
        
        d = res['hits']['hits'][0]['_source']['gaming_date']['full_date']
        last_update = utc_to_local(parse(d)).date()
        start_date = last_update + datetime.timedelta(days=1)
        today = datetime.datetime.now().date()
        end_date = today - datetime.timedelta(days=1)
        if start_date == end_date:
            pit_trips_etl(start_date)
        else:
            dates = pd.date_range(start_date, end_date).tolist()
            for date in dates:
                pit_trips_etl(date)
    except Exception, e:
            elastic_logger.exception(e)
    elastic_logger.info("Update complete")

@shared_task
def update_pit_session_recs():
    elastic_logger.info("Updating elasticsearch Slot Session Documents" )
    try:
        es = Elasticsearch([es_host])
        query = {
            'query': {
                'match_all': {},
            },
            'sort': {
                    'gaming_date.full_date': {"order": "desc"}
            },
            'size': '1'
        }
        res = es.search(index='pit_sessions', body=query)
        
        d = res['hits']['hits'][0]['_source']['gaming_date']['full_date']
        last_update = utc_to_local(parse(d))
        start_date = last_update + datetime.timedelta(days=1)
        today = datetime.datetime.now().date()
        end_date = today - datetime.timedelta(days=1)
        if start_date == end_date:
            pit_sessions_etl(start_date)
        else:
            dates = pd.date_range(start_date, end_date).tolist()
            for date in dates:
                pit_sessions_etl(date)
    except Exception, e:
            elastic_logger.exception(e)
    elastic_logger.info("Update complete")
    
@shared_task
def update_headcount_recs():
    elastic_logger.info("Updating elasticsearch Headcount Documents" )
    try:
        es = Elasticsearch([es_host])
        query = {
            'query': {
                'match_all': {},
            },
            'sort': {
                    'gaming_date.full_date': {"order": "desc"}
            },
            'size': '1'
        }
        res = es.search(index='slot_headcount', body=query)
        
        d = res['hits']['hits'][0]['_source']['gaming_date']['full_date']
        last_update = utc_to_local(parse(d))
        start_date = last_update + datetime.timedelta(days=1)
        today = datetime.datetime.now().date()
        end_date = today - datetime.timedelta(days=1)
        if start_date == end_date:
            headcount_etl(start_date)
        else:
            dates = pd.date_range(start_date, end_date).tolist()
            for date in dates:
                headcount_etl(date)
    except Exception, e:
            elastic_logger.exception(e)
    elastic_logger.info("Update complete")
    
def update_all():
    update_slot_revenue_recs()
    update_slot_trip_recs()
    update_slot_session_recs()
    update_pit_revenue_recs()
    update_pit_trip_recs()
    update_pit_session_recs()
    update_headcount_recs()
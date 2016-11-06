# -*- coding: utf-8 -*-
"""
Created on Sat Feb 06 15:48:10 2016

@author: Lathropk
"""
from preserialize.serialize import serialize
from django.conf import settings
from oasis_extract import slot_revenue_extract, pit_revenue_extract
from transform import transform_slot_revenue, transform_pit_revenue
from elasticsearch import Elasticsearch, helpers

es_host = settings.ES_HOST


def slot_revenue_etl(audit_date):
    es = Elasticsearch([es_host])
    batch_chunks = []
    iterator = 0  
    revenue_ext = slot_revenue_extract(audit_date)
    revenue_trans = transform_slot_revenue(audit_date, revenue_ext)
    for rec in revenue_trans:
        s = serialize(rec)
        id_ = str(s['slotgame']['slot_number']) + '_' + str(s['gaming_date']['datekey'])
        data_dict = {
                "_index": "slot_revenue", 
                "_type": "slot_revenue",
                "_id": id_,
                "_source": s
        }
        
        batch_chunks.append(data_dict)
        if iterator % 100 == 0:
            helpers.bulk(es, batch_chunks, request_timeout=60)
            del batch_chunks[:]
        iterator = iterator + 1
    
    if len(batch_chunks) != 0:
            helpers.bulk(es, batch_chunks)

def pit_revenue_etl(audit_date):
    es = Elasticsearch([es_host])
    batch_chunks = []
    iterator = 0  
    drop_ext = pit_revenue_extract(audit_date)
    drop_trans = transform_pit_revenue(audit_date, drop_ext)
    for rec in drop_trans:
        s = serialize(rec)
        id_ = s['drop_id']
        data_dict = {
                "_index": "pit_revenue", 
                "_type": "pit_drop",
                "_id": id_,
                "_source": s
        }
        
        batch_chunks.append(data_dict)
        if iterator % 100 == 0:
            helpers.bulk(es, batch_chunks, request_timeout=60)
            del batch_chunks[:]
        iterator = iterator + 1
    
    if len(batch_chunks) != 0:
            helpers.bulk(es, batch_chunks)
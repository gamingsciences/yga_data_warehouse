# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:53:27 2016

@author: lathropk
"""
from preserialize.serialize import serialize
from django.conf import settings
from oasis_extract import headcount_extract
from transform import transform_headcount
from elasticsearch import Elasticsearch, helpers

es_host = settings.ES_HOST


def headcount_etl(audit_date):
    es = Elasticsearch([es_host])
    batch_chunks = []
    iterator = 0  
    revenue_ext = headcount_extract(audit_date)
    revenue_trans = transform_headcount(revenue_ext)
    for rec in revenue_trans:
        s = serialize(rec)
        id_ = str(rec['headcount_id'])
        data_dict = {
                "_index": "slot_headcount", 
                "_type": "headcount",
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


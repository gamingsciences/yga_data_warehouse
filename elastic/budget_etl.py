# -*- coding: utf-8 -*-
"""
Created on Fri Sep 30 14:53:27 2016

@author: lathropk
"""
from preserialize.serialize import serialize
from django.conf import settings
from conformed_dimensions.models import DailyBudgetDimension
from transform import transform_daily_budget
from elasticsearch import Elasticsearch, helpers

es_host = settings.ES_HOST


def budget_etl():
    es = Elasticsearch([es_host])
    batch_chunks = []
    iterator = 0  
    budget_ext = DailyBudgetDimension.objects.all().values()
    budget_trans = transform_daily_budget(budget_ext)
    for rec in budget_trans:
        s = serialize(rec)
        id_ = str(s['location']['casino']) + '_' + str(s['gaming_date']['datekey'])
        data_dict = {
                "_index": "daily_budget", 
                "_type": "daily_budget",
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


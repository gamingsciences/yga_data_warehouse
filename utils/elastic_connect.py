# -*- coding: utf-8 -*-
"""
Created on Tue Sep 13 09:08:19 2016

@author: Lathropk
"""

import requests
import json
from django.conf import settings

from elasticsearch import Elasticsearch, helpers

es_host = settings.ES_HOST

def search(idx, query):
    es = Elasticsearch([es_host])
    res = es.search(index=idx, body=query)
    return res

query = {
    'query': {
        'match_all': {},
    },
    'sort': {
            'audit_date.full_date': {"order": "desc"}
    },
    'size': '1'
}

rec=search('slot_revenue', query)


def reindex(analysisSettings={}, mappingSettings={}, movieDict={}):
    settings = { #A
        "settings": {
            "number_of_shards": 1, #B
            "index": {
                "analysis" : analysisSettings, #C
            }}}

    if mappingSettings:
        settings['mappings'] = mappingSettings #C

    resp = requests.delete("http://localhost:9200/tmdb") #D
    resp = requests.put("http://localhost:9200/tmdb", 
                        data=json.dumps(settings))

    bulkMovies = ""
    print "building..."
    for id, movie in movieDict.iteritems(): 
        addCmd = {"index": {"_index": "tmdb", #E
                            "_type": "movie",
                            "_id": movie["id"]}}
        bulkMovies += json.dumps(addCmd) + "\n" + json.dumps(movie) + "\n"

    print "indexing..."
    resp = requests.post("http://localhost:9200/_bulk", data=bulkMovies)

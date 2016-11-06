# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 15:17:43 2016

@author: lathropk
"""
from elasticsearch import Elasticsearch
import pandas as pd


es_host = "https://query:query86304@33c192f38ba000038f45d61b4fe43cac.us-east-1.aws.found.io:9243/"


def sample_query():
    es = Elasticsearch([es_host])
    query = {
              "size": 10000,
              "_source": ["player.player_id",
                          "player.full_name",
                          "player.address_a",
                          "player.city",
                          "player.state",
                          "player.zip"],
              "query": {
                "constant_score": {
                  "filter": {
                    "bool": {
                      "must": [
                        {
                          "range": {"player.distance": {"gt": 100}}
                        },
                        {
                          "range": {"clv": {"gt": 100}}
                        },
                        {
                          "range": {
                            "gaming_date.full_date": {
                              "gte": "2016-10-31",
                              "lte": "2016-10-31"
                            }
                          }
                        }
                      ]
                    }
                  }
                }
              }
            }
    res = es.search(index='slot_player_stats', body=query)
    recs = res['hits']['hits']
    result_set = [rec['_source']['player'] for rec in recs]
    
    return pd.DataFrame(result_set)
    
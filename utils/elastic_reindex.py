# -*- coding: utf-8 -*-
"""
Reindex an elasticsearch index

Use the following code in conjuntion with the ES console to re-index an index
in elasticsearch.
"""
from django.conf import settings
from elasticsearch import Elasticsearch, helpers

es_host = settings.ES_HOST

es = Elasticsearch([es_host], verify_certs=False, timeout=600)

# this is the index you want to re-index
source_index = 'pit_trips'
# this will be the new index.  It should have a name like 'my_index_v2'
target_index = 'pit_trips_v2'
# this will be the new index alias
alias = ''

# before you run the reindex, create the target index in the console and add 
# the new mapping

helpers.reindex(client=es, 
                source_index=source_index, 
                target_index=target_index, 
                target_client=es)
# check the new target index in kibana, and if it looks good, point it to the alias 
es.indices.put_alias(index=target_index, name=alias)

# if all went well - delete the source index

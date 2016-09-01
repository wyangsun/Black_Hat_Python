from elasticsearch import Elasticsearch
import time

TIMESTAMP="%Y%m%d%H%M%S"
from_time="20160901000002"
to_time = "20160901070001"

file = open('es.log','w')

milli_time = lambda x: int(round(time.mktime(time.strptime(x,TIMESTAMP)) * 1000))

es = Elasticsearch([
            {'host': '127.0.0.1'},
        ])

body_json = {
  "query": {
    "filtered": {
      "query": {
        "query_string": {
          "analyze_wildcard": "true",
          "query": "*"
        }
      },
      "filter": {
        "bool": {
          "must": [
            {
              "range": {
                "@timestamp": {
                  "gte": milli_time(from_time),
                  "lte": milli_time(to_time),
                  "format": "epoch_millis"
                }
              }
            }
          ],
          "must_not": []
        }
      }
    }
  }
}

abc = es.search(index="logstash-2016.09.01",sort='@timestamp',_source_include="message",body=body_json,size=10000)
for x in abc['hits']['hits']:
  s = x['_source']['message'].encode('utf-8') + '\n'
  file.writelines(s)
file.close()

import json
import os
import random
from datetime import datetime, timedelta

from elasticsearch import Elasticsearch
import pytz

USER = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]


def write_data():
    users = [f"user-{i}" for i in range(10)]

    # covert to UTC timezone
    utc = pytz.UTC
    taipei = pytz.timezone("Asia/Taipei")
    start = taipei.localize(datetime.now() - timedelta(days=1)).astimezone(utc)
    end = taipei.localize(datetime.now()).astimezone(utc)

    for i in range(10000):
        # create a row with random user and random value
        ts = start + (end - start) * random.random()
        doc = {
            "user": random.choice(users),
            "value": random.randint(1, 100),
            "timestamp": ts.strftime("%Y-%m-%dT%H:%M:%SZ"),
        }
        print(ts.strftime("%Y-%m-%dT%H:%M:%SZ"))
        es.index(index=index_name, body=json.dumps(doc))


def read_data():
    res = es.search(index="ivan_index", body={"query": {"match_all": {}}})

    print(f'Got  {res["hits"]["total"]["value"]}')
    for row in res["hits"]["hits"]:
        print(row["_source"])


def count_value(user="user-1"):
    query = {
        "query": {"match": {"user": "user-1"}},
        "size": 0,
        "aggs": {"total_value": {"sum": {"field": "value"}}},
    }
    response = es.search(index=index_name, body=query)
    total_value = response["aggregations"]["total_value"]["value"]
    print(f"Total value for user {user}:", total_value)


if __name__ == "__main__":
    # create a  Elasticsearch connection
    es = Elasticsearch(
        ["https://elasticsearch-master:9200"],
        basic_auth=(USER, PASSWORD),
        verify_certs=False,
    )


# create index if not exist
index_name = "ivan_index"
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)
    write_data()

count_value()
# read_data()

import pandas as pd
import pymongo
import json
from datetime import datetime

mongo_client = pymongo.MongoClient("mongodb+srv://Max:<password>@cluster0.qv5ym.mongodb.net/myFirstDatabase"
                                   "?retryWrites=true&w=majority")
mongo_database = mongo_client['Covid19Cases']
collection_name = 'Cases'
database_collection = mongo_database[collection_name]
reserve_database = mongo_client['Reserve']
reserve_collection_name = 'backup'
reserve_collection = reserve_database[reserve_collection_name]


def import_data(filepath):
    data = pd.read_csv(filepath)
    data_json = json.loads(data.to_json(orient='records'))
    database_collection.remove()
    database_collection.insert(data_json)


def get_by_filter(criteria):
    results = pd.DataFrame(database_collection.find(criteria))
    results = filter_data(results)
    return results


def get_one(criteria):
    results = pd.DataFrame(database_collection.find_one(criteria))
    results = filter_data(results)
    return results


def insert(item=None):
    database_collection.insert(item)


def create_backup():
    results = pd.DataFrame(database_collection.find({}))
    results.to_csv('./tmp/buffer.csv')
    data = pd.read_csv('./tmp/buffer.csv')
    data_json = json.loads(data.to_json(orient='records'))
    reserve_collection.remove()
    reserve_collection.insert(data_json)


def filter_data(dataframe):
    dataframe = dataframe.fillna(0)
    dataframe = dataframe.drop_duplicates(subset=['day', 'countriesAndTerritories', 'year', 'month'])
    return dataframe



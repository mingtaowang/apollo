# -*- coding: utf-8 -*-

from pymongo import MongoClient

from apollo.config import MONGODB_DATABASE_SERVER

db_mongo = MongoClient(MONGODB_DATABASE_SERVER.get('uri'), maxPoolSize=MONGODB_DATABASE_SERVER.get('pool_size'))

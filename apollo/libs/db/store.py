# -*- coding: utf-8 -*-

import redis

from pymongo import MongoClient

from apollo.config import MONGODB_DATABASE_SERVER, REDIS_DATABASE_SERVER

db_mongo = MongoClient(MONGODB_DATABASE_SERVER.get('uri'), maxPoolSize=MONGODB_DATABASE_SERVER.get('pool_size'))

r = redis.Redis(host=REDIS_DATABASE_SERVER.get('host'),
                port=REDIS_DATABASE_SERVER.get('port'),
                db=REDIS_DATABASE_SERVER.get('db'))

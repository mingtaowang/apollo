# -*- coding: utf-8 -*-

DEBUG = True

HTTP_PORT = 5000

if DEBUG:
    HTTP_HOST = '127.0.0.1'
    MONGODB_DATABASE_SERVER = {"uri": "mongodb://104.225.151.165:9999", "pool_size": 4}
    REDIS_DATABASE_SERVER = {"host": "104.225.151.165", "port": 6379, "db": 0}
else:
    HTTP_HOST = '104.225.151.165'
    MONGODB_DATABASE_SERVER = {"uri": "mongodb://104.225.151.165:9999", "pool_size": 4}
    REDIS_DATABASE_SERVER = {"host": "104.225.151.165", "port": 6379, "db": 0}

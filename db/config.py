""" Database Connection File"""

from pymongo import MongoClient

# CLIENT
CLIENT = MongoClient('localhost', 27017)

# DATABASE
DB = CLIENT['MovieApp']

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import os
from sys import exit
import logging

# Exit if it's not possible to connect to DB
MONGO_URI = os.environ.get('MONGO_URI')

if not MONGO_URI:
    logging.error("No MONGO_URI was defined. exiting.")
    exit(1)

try:
    db_connection = MongoClient(MONGO_URI)
    db = db_connection.clients
    collection = db["users"]
except ConnectionFailure:
    logging.error("Cannot connect to DB")
except Exception:
    logging.error("Something went wrong")

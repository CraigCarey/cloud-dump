from kafka import KafkaConsumer
from pymongo import MongoClient
from json import loads

topic = 'numtest'
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',  # where to restart reading after disconnect
    enable_auto_commit=True,  # commit the read offset every interval
    group_id='counters',
    value_deserializer=lambda x: loads(x.decode('utf-8')))

db_client = MongoClient('localhost:27017')
collection = db_client.numtest.numtest

for message in consumer:
    message = message.value
    collection.insert_one(message)
    print('{} added to {}'.format(message, collection))

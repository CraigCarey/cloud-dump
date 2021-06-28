from time import sleep
from json import dumps
from kafka import KafkaProducer


def on_send_success(record_metadata):
    print("on_send_success:topic", record_metadata.topic)
    print("on_send_success:partition", record_metadata.partition)
    print("on_send_success:offset", record_metadata.offset)


def on_send_error(excp):
    print("on_send_error", excp)


# value_serializer: how the data should be serialized - convert to json and encode as utf-8
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x:
                         dumps(x).encode('utf-8'))

topic = 'numtest'

for e in range(1000):
    data = {'number': e}
    fut = producer.send(topic, value=data)
    fut.add_callback(on_send_success)
    fut.add_errback(on_send_error)
    sleep(3)

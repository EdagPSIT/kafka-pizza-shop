from kafka import KafkaProducer
from json import dumps
from pizzaproducer import PizzaProvider
import time
from faker import Faker

ORDER_DETAIL_TOPIC_NAME = 'pizza_order_details'
producer = KafkaProducer(bootstrap_servers=['localhost:9092'],
                         value_serializer=lambda x: dumps(x).encode('utf-8'),
                         key_serializer=lambda x: x.encode('utf-8'))

fakerobject = Faker()
while True:
    pizaa = PizzaProvider(fakerobject)
    pizzaorder, key = pizaa.produce_msg(fakerobject)
    producer.send(ORDER_DETAIL_TOPIC_NAME, key=str(key), value=pizzaorder)
    time.sleep(5)

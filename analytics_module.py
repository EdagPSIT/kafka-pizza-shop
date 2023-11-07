from kafka import KafkaConsumer
from json import loads,dumps

ORDER_DETAIL_TOPIC_NAME = 'pizza_order_details'
ORDER_CONFIRMED_TOPIC_NAME = 'pizza_order_confirmed'
consumer_order_details = KafkaConsumer(ORDER_DETAIL_TOPIC_NAME,bootstrap_servers='localhost:9092')
consumer_order_confirmed = KafkaConsumer(ORDER_CONFIRMED_TOPIC_NAME,bootstrap_servers='localhost:9092')


total_orders = 0
total_confirmed_orders = 0
while True:
    for message in consumer_order_details:
        orders_message = loads(message.value.decode())
        total_orders = total_orders + 1
        print('Total orders are {}'.format(total_orders))

    for message in consumer_order_confirmed:
        confirmed_orders_message = loads(message.value.decode())
        total_confirmed_orders = total_confirmed_orders + 1
        print('Total confirmed orders are {}'.format(total_confirmed_orders))

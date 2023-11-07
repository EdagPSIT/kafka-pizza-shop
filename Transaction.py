from kafka import KafkaConsumer,KafkaProducer
from json import loads,dumps


ORDER_DETAIL_TOPIC_NAME = 'pizza_order_details'
ORDER_CONFIRMED_TOPIC_NAME = 'pizza_order_confirmed'

consumer = KafkaConsumer(ORDER_DETAIL_TOPIC_NAME,bootstrap_servers = 'localhost:9092')
producer = KafkaProducer(bootstrap_servers='localhost:9092')

print("Pizza order details are.........")
while True:
    for message in consumer:
        print('pizza_order details')
        message = loads(message.value.decode())
        print(message)
        print('='*50)

        # Write a message to order confiremed topic

        data = {
            'user': '{} {}'.format(message['first_name'],message['first_name']),
            'email': message['Email'],
            'total_pizzas_ordered': len(message['pizzas']),
            'Pizza Details': message['pizzas']
        }
        producer.send(ORDER_CONFIRMED_TOPIC_NAME,dumps(data).encode('utf-8'))
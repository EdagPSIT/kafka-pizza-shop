from kafka import KafkaConsumer
from json import loads,dumps


ORDER_CONFIRMED_TOPIC_NAME = 'pizza_order_confirmed'

consumer_order_confirmed = KafkaConsumer(ORDER_CONFIRMED_TOPIC_NAME,bootstrap_servers='localhost:9092')


while True:
    for message in consumer_order_confirmed:
        cnmd_meaage = loads(message.value.decode())
        print('Hello {},'.format(cnmd_meaage['user']))
        print("You have orderd total {} pizzas and details are below.".format(cnmd_meaage['total_pizzas_ordered']))
        print('Pizza Details')
        for pizza in cnmd_meaage['Pizza Details']:
            print('Pizza Name: {}'.format(pizza['pizzaName']))
            if len(pizza['additionalToppings'])>0:
                print('Additional Toppings: {} '.format(pizza['additionalToppings']))
        print("\n\n We appreciate your order!\n\n Enjoy your meal, and please remember to share your feedback on the taste.")
        print('='*90)
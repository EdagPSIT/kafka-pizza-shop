import random
import time
from faker.providers import BaseProvider

class PizzaProvider(BaseProvider):
    def __init__(self, generator):
        super().__init__(generator)
    def pizza_name(self):
        valid_pizza_names = [
            "Margherita",
            "Marinara",
            "Diavola",
            "Mari & Monti",
            "Salami",
            "Peperoni",
        ]
        return random.choice(valid_pizza_names)

    def pizza_topping(self):
        available_pizza_toppings = [
            "🍅 tomato",
            "🧀 blue cheese",
            "🥚 egg",
            "🫑 green peppers",
            "🌶️ hot pepper",
            "🥓 bacon",
            "🫒 olives",
            "🧄 garlic",
            "🐟 tuna",
            "🧅 onion",
            "🍍 pineapple",
            "🍓 strawberry",
            "🍌 banana",
        ]
        return random.choice(available_pizza_toppings)

    def pizza_shop(self):
        pizza_shop_names = [
            "Pizza Haven",
            "Slice House",
            "Crust Corner",
            "Dough Delight",
            "Tasty Pies",
            "Cheese Heaven",
            "Oven Fresh",
            "Pepperoni Palace",
            "Sizzle Spot",
            "Mamma's Kitchen"
        ]
        return random.choice(pizza_shop_names)

    def produce_msg(self, faker_object, max_pizzas_in_order=5, max_toppings_in_pizza=3):
        order_count = 1
        shop = self.pizza_shop()
        # Each Order can have 1-10 pizzas in it
        pizzas = []
        for pizza in range(random.randint(1, max_pizzas_in_order)):
            # Each Pizza can have 0-5 additional toppings on it
            toppings = []
            for topping in range(random.randint(0, max_toppings_in_pizza)):
                toppings.append(self.pizza_topping())
            pizzas.append(
                {
                    "pizzaName": self.pizza_name(),
                    "additionalToppings": toppings,
                }
            )


        first_name = faker_object.first_name()
        last_name = faker_object.first_name()
        domain = faker_object.domain_name()
        message = {
            #"id": order_count,
            "shop": shop,
            "first_name": first_name,
            'last_name': last_name,
            'Email': '{}.{}@{}'.format(first_name,last_name,domain),
            "phoneNumber": faker_object.unique.phone_number(),
            "address": faker_object.address(),
            "pizzas": pizzas,
            "timestamp": int(time.time() * 1000),
        }
        key = {"shop": shop}
        order_count += 1
        return message, key

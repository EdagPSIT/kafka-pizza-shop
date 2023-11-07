# Kafka Food Order System

### WorkFlow 
![Untitled Diagram drawio](https://github.com/EdagPSIT/kafka-pizza-shop/assets/134361096/19f2ba87-ee40-42cb-8336-1e0bd36374aa)



This project consists of four main modules: Food Order App, Transactional Module, Email Module, and Analytic Module, all integrated with a Kafka cluster. The system is designed to simulate a pizza ordering application.
Modules
#### 1. Food Order App

The Food Order App module utilizes the faker library and Python to generate orders similar to those of a real pizza shop. Each order includes customer details, shop information, address, pizza types, and toppings. Additionally, users can place orders for multiple pizzas in a single transaction. The orders generated by this module are then published to the order_details topic within the Kafka cluster.

#### 2. Transactional Module
The Transactional Module subscribes to the order_details topic and processes the incoming orders. It also sends an order_confirmed topic to the Kafka cluster upon successful order processing.

#### 3. Email Module
The Email Module subscribes to the order_confirmed topic within the Kafka cluster. Upon receiving a message, it handles the notification process, sending order confirmation emails to customers.

#### 4. Analytic Module
The Analytic Module is responsible for processing and analyzing the data from the order_details topic. It provides insights and analytics on the orders received and processed within the system.
Getting Started

To get started with this Kafka Food Order System, follow the instructions below:
- Install Kafka on your system and set up a Kafka cluster.
- Set up the required dependencies for each module. Ensure that the necessary Python packages and libraries are installed.
- Run the modules in the following order: Food Order App, Transactional Module, Email Module, and Analytic Module.

Dependencies

- Kafka
- Python
- Faker library

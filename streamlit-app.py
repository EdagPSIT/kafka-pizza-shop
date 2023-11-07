import streamlit as st
from kafka import KafkaConsumer
from json import loads
import threading
import pandas as pd

TOPIC_NAME = 'pizza'
messages = []

# Function to receive messages from Kafka
def receive_messages():
    consumer = KafkaConsumer(
        TOPIC_NAME,
        bootstrap_servers=['localhost:9092'],
        auto_offset_reset='earliest',
        enable_auto_commit=True,
        group_id=None,
        value_deserializer=lambda x: loads(x.decode('utf-8')))

    for message in consumer:
        messages.append(message.value)

# Run Kafka consumer in a separate thread
thread = threading.Thread(target=receive_messages)
thread.start()

# Create a Streamlit app
st.title('Pizza Orders from Kafka')
placeholder = st.empty()

# Function to display messages in a DataFrame
def display_messages(messages):
    if messages:
        #df = pd.DataFrame(messages, columns=['Order'])
        placeholder.write(messages)
    else:
        placeholder.write("No messages yet.")

# Display messages in the Streamlit app
while True:
    display_messages(messages)

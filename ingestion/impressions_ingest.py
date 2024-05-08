import json
from kafka import KafkaConsumer

# Purpose: This script will ingest ad impressions data in real-time (using Kafka or a similar message broker) or from a batch source.

def ingest_impressions(topic):
    """
    Function to consume ad impression data from a Kafka topic.
    """
    consumer = KafkaConsumer(
        topic,
        bootstrap_servers='localhost:9092',  # Adjust this to your broker's address
        auto_offset_reset='earliest',  # Start from the earliest message in the topic
        enable_auto_commit=True,
        group_id='impressions-consumer-group'
    )
    for message in consumer:
        impression_data = json.loads(message.value)
        # Process or store the data as needed
        print(f"Received impression data: {impression_data}")

if __name__ == "__main__":
    ingest_impressions('impressions_topic')

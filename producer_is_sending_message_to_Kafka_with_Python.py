from kafka import KafkaProducer

producer = KafkaProducer(bootstrap_servers='localhost:9092')
producer.send('test-topic', b'This Message is sent by Mohamed Reda in Python with kafka-python to Kafka')
producer.flush()
print("Message sent!")

"""
This Message is have ben got by Mohamed Reda in Python with kafka-python
"""

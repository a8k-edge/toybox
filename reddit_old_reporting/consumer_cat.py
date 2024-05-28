from confluent_kafka import Consumer, KafkaError


topic = 'analytics.users.requests'
consumer = Consumer({
    'bootstrap.servers': 'localhost:9092',
    'security.protocol': 'PLAINTEXT',
    'group.id': 'group-1',  
    'auto.offset.reset': 'earliest',
})
consumer.subscribe([topic])
try:
    while True:
        msg = consumer.poll(1.0)
        if msg is not None and msg.error():
            if msg.error().code() == KafkaError._PARTITION_EOF:
                print('Partition EOF')
        
        if msg is not None and msg.error() is None:
            key = msg.key().decode('utf-8')
            value = msg.value().decode('utf-8')
            print(f'Consumed message from topic {topic}: key = {key:12} value = {value:12}')
except KeyboardInterrupt:
    pass
finally:
    consumer.close()

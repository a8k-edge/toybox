from confluent_kafka import Consumer
import socket
import yaml


if __name__ == '__main__':
    config = {}
    with open('config.yaml') as stream:
        config = yaml.safe_load(stream) 

    conf = {'bootstrap.servers': config['server'],
            'security.protocol': 'SASL_SSL',
            'sasl.mechanism': 'PLAIN',
            'sasl.username': config['api_key'],
            'sasl.password': config['api_secret'],
            'client.id': socket.gethostname()}
    conf['group.id'] = 'group-1'
    conf['auto.offset.reset'] = 'earliest'
    topic = config['topic']

    consumer = Consumer(conf)
    consumer.subscribe([topic])

    try:
        while True:
            msg = consumer.poll(1.0)
            if msg is not None and msg.error() is None:
                key = msg.key().decode('utf-8')
                value = msg.value().decode('utf-8')
                print(f'Consumed message from topic {topic}: key = {key:12} value = {value:12}')
    except KeyboardInterrupt:
        pass
    finally:
        consumer.close()
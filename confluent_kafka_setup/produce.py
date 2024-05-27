from confluent_kafka import Producer
import socket
import yaml


def delivery_report(err, msg):
    '''
    Reports the success or failure of a message delivery.

    Args:
        err (KafkaError): The error that occurred on None on success.
        msg (Message): The message that was produced or failed.
    '''

    if err is not None:
        print('Delivery failed for User record {}: {}'.format(msg.key(), err))
        return
    print('User record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))

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
    topic = config['topic']

    producer = Producer(conf)

    while True:
        producer.poll(0.0)
        try:
            key = input('Enter key: ')
            value = input('Enter value: ')
            producer.produce(topic=topic,
                                key=key,
                                value=value,
                                on_delivery=delivery_report)
        except KeyboardInterrupt:
            break
        except ValueError:
            print('Invalid input, discarding record...')
            continue

        print('\nFlushing records...')
        producer.flush()

    print(producer)
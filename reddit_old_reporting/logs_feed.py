import time
import datetime
import numpy
import random
import json
import logging, time
import socket
from tzlocal import get_localzone

from faker import Faker
from confluent_kafka import Producer


local = get_localzone()
topic = 'analytics.users.requests'


def main():
    producer = Producer({'bootstrap.servers': 'localhost:9092',
            'security.protocol': 'PLAINTEXT',
            'client.id': socket.gethostname()})

    while True:
        faker = Faker()

        otime = datetime.datetime.now()

        verb=['GET','POST','DELETE','PUT']
        ualist=[faker.firefox, faker.chrome, faker.safari, faker.internet_explorer, faker.opera]
        headers=['HEADER','PING']
        ip = faker.ipv4()
        dt = otime.strftime('%d/%b/%Y:%H:%M:%S')
        tz = datetime.datetime.now(local).strftime('%z')
        vrb = numpy.random.choice(verb,p=[0.6,0.1,0.1,0.2])
        header = numpy.random.choice(headers,p=[0.3,0.7])

        resp = '200'
        byt = str(int(random.gauss(5000,50)))
        referer = faker.uri_path()
        useragent = numpy.random.choice(ualist,p=[0.5,0.3,0.1,0.05,0.05] )()

        message_json = {
            'header':header,
            'ip':ip,
            'dt':dt,
            'tz':tz,
            'vrb':vrb,
            'resp':resp,
            'byt':byt,
            'referer':referer,
            'useragent':useragent
        }
        
        producer.produce(topic=topic,
                         key=header,
                         value=json.dumps(message_json),
                         on_delivery=delivery_report)
        producer.flush()
        
        time.sleep(0.5)


def delivery_report(err, msg):
    if err is not None:
        print('Delivery failed for {}: {}'.format(msg.key(), err))
        return
    print('Record {} successfully produced to {} [{}] at offset {}'.format(
        msg.key(), msg.topic(), msg.partition(), msg.offset()))


if __name__ == '__main__':
    logging.basicConfig(
        format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
        level=logging.INFO
    )
    main()
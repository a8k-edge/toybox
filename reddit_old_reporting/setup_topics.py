from confluent_kafka import admin


new_topic = admin.NewTopic('analytics.users.requests', num_partitions=1)
admin_client = admin.AdminClient({
    'bootstrap.servers': 'localhost:9092',
    'security.protocol': 'PLAINTEXT',
})
fs = admin_client.create_topics([new_topic], operation_timeout=10, request_timeout=10)
print(fs)

for topic, f in fs.items():
    try:
        f.result()
        print("Topic {} created".format(topic))
    except Exception as e:
        print("Failed to create topic {}: {}".format(topic, e))

from confluent_kafka import admin, KafkaException


admin_client = admin.AdminClient({
    'bootstrap.servers': 'localhost:9092',
    'security.protocol': 'PLAINTEXT',
})
cluster_metadata = admin_client.list_topics(timeout=10)

print("Cluster Metadata:")
print(f"Broker count: {len(cluster_metadata.brokers)}")
for broker in cluster_metadata.brokers.values():
    print(f"Broker ID: {broker.id}, Host: {broker.host}, Port: {broker.port}")

print("***"*10)
print("Topic Metadata:")
for topic, metadata in cluster_metadata.topics.items():
    print(f"Topic: {topic}", len(metadata.partitions))
    # for partition_id, partition in metadata.partitions.items():
    #     print(f"  Partition: {partition_id}")
    #     print(f"    Leader: {partition.leader}")
    #     print(f"    Replicas: {partition.replicas}")
    #     print(f"    ISRs: {partition.isrs}")

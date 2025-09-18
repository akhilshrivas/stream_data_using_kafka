import json
from kafka import KafkaConsumer

consumer = KafkaConsumer(
    "test-topic",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    group_id="streaming-group",
    value_deserializer=lambda v: json.loads(v.decode("utf-8")) if v else None
)

print("Listening for messages...")
for msg in consumer:
    print("Received:", msg.value)
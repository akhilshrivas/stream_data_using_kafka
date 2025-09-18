
import time, json
from kafka import KafkaProducer
from datetime import datetime

producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

while True:
    msg = {"user": "Akhil", "action": "login", "timestamp": datetime.utcnow().isoformat()}
    producer.send("test-topic", msg)
    print("Sent:", msg)
    time.sleep(5)

import os
from dotenv import load_dotenv


load_dotenv()

MQTT_BROKER = os.getenv("MQTT_BROKER")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_USERNAME = os.getenv("MQTT_USERNAME")
MQTT_PASSWORD = os.getenv("MQTT_PASSWORD")
TOPIC_PREFIX = os.getenv("TOPIC_PREFIX", "iot/secure")
PUBLISH_INTERVAL = int(os.getenv("PUBLISH_INTERVAL", 5))
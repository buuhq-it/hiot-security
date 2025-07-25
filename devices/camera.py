import paho.mqtt.client as mqtt
import time, json, random

import config

def create_payload():
    return json.dumps({
        "device_id": "cam-001",
        "mac_address": "11:22:33:44:55:66",
        "motion_detected": int(random.choice([True, False])),
        "brightness": random.randint(0, 100),
        "timestamp": time.time()
    })

def run():
    client = mqtt.Client(client_id="cam-001")
    client.username_pw_set(config.MQTT_USERNAME, config.MQTT_PASSWORD)
    client.connect(config.MQTT_BROKER, config.MQTT_PORT)

    while True:
        payload = create_payload()
        client.publish(f"{config.TOPIC_PREFIX}/camera", payload)
        print("Camera sent:", payload)
        time.sleep(5)

if __name__ == "__main__":
    run()

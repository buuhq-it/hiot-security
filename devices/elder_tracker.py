
import paho.mqtt.client as mqtt
import time, json, random
import config

def create_payload():
    return json.dumps({
        "device_id": "elder-001",
        "mac_address": "AA:BB:CC:DD:EE:01",
        "fall_detected": int(random.choice([True, False])),
        "gps_location": {
            "lat": round(random.uniform(10.76, 10.78), 6),
            "lon": round(random.uniform(106.68, 106.70), 6)
        },
        "timestamp": time.time()
    })

def run():
    client = mqtt.Client(client_id="elder-001")
    client.username_pw_set(config.MQTT_USERNAME, config.MQTT_PASSWORD)
    client.connect(config.MQTT_BROKER, config.MQTT_PORT)

    while True:
        payload = create_payload()
        client.publish(f"{config.TOPIC_PREFIX}/elder_tracker", payload)
        print("Elder Tracker sent:", payload)
        time.sleep(7)

if __name__ == "__main__":
    run()

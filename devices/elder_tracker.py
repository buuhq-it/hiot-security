
import paho.mqtt.client as mqtt
import time, json, random

def create_payload():
    return json.dumps({
        "device_id": "elder-001",
        "mac_address": "AA:BB:CC:DD:EE:01",
        "fall_detected": random.choice([True, False]),
        "gps_location": {
            "lat": round(random.uniform(10.76, 10.78), 6),
            "lon": round(random.uniform(106.68, 106.70), 6)
        },
        "timestamp": time.time()
    })

def run():
    client = mqtt.Client(client_id="elder-001")
    client.username_pw_set("iot", "Password123")
    client.connect("mqtt.technote.online", 1883)

    while True:
        payload = create_payload()
        client.publish("paper_wifi/test/elder_tracker", payload)
        print("Elder Tracker sent:", payload)
        time.sleep(7)

if __name__ == "__main__":
    run()

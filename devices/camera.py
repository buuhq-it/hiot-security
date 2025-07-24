import paho.mqtt.client as mqtt
import time, json, random

def create_payload():
    return json.dumps({
        "device_id": "cam-001",
        "mac_address": "11:22:33:44:55:66",
        "motion_detected": random.choice([True, False]),
        "brightness": random.randint(0, 100),
        "timestamp": time.time()
    })

def run():
    client = mqtt.Client(client_id="cam-001")
    client.username_pw_set("iot", "Password123")
    client.connect("mqtt.technote.online", 1883)

    while True:
        payload = create_payload()
        client.publish("paper_wifi/test/camera", payload)
        print("Camera sent:", payload)
        time.sleep(5)

if __name__ == "__main__":
    run()

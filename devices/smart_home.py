
import paho.mqtt.client as mqtt
import time, json, random

def create_payload():
    return json.dumps({
        "device_id": "home-001",
        "mac_address": "AA:BB:CC:DD:EE:02",
        "temperature": round(random.uniform(25.0, 30.0), 1),
        "humidity": random.randint(40, 60),
        "gas_leak": random.choice([False, False, True]),
        "timestamp": time.time()
    })

def run():
    client = mqtt.Client(client_id="home-001")
    client.username_pw_set("iot", "Password123")
    client.connect("mqtt.technote.online", 1883)

    while True:
        payload = create_payload()
        client.publish("paper_wifi/test/smart_home", payload)
        print("Smart Home sent:", payload)
        time.sleep(6)

if __name__ == "__main__":
    run()

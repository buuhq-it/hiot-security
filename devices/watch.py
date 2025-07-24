import paho.mqtt.client as mqtt
import time, random, json

def create_payload():
    return json.dumps({
        "device_id": "watch-001",
        "mac_address": "A1:B2:C3:D4:E5:F6",
        "heart_rate": random.randint(60, 100),
        "temperature": round(random.uniform(36.5, 37.5), 1),
        "timestamp": time.time()
    })

def run():
    client = mqtt.Client(client_id="watch-001")
    client.username_pw_set("iot", "Password123")
    client.connect("mqtt.technote.online", 1883)

    while True:
        payload = create_payload()
        client.publish("paper_wifi/test/watch", payload)
        print("Watch sent:", payload)
        time.sleep(3)

if __name__ == "__main__":
    run()

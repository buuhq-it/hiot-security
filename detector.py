# detector.py

import paho.mqtt.client as mqtt
import json
import config
from datetime import datetime

from rules import check_rules

# MQTT config
# MQTT_BROKER = "localhost"
# MQTT_PORT = 1883
# MQTT_TOPIC = "paper_wifi/test/#"
# MQTT_USERNAME = "iot"
# MQTT_PASSWORD = "Password123"

# Hàm khi nhận tin nhắn
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        alerts = check_rules(payload)

        if alerts:
            print(f"[{datetime.now().isoformat()}] 📣 PHÁT HIỆN BẤT THƯỜNG:")
            for alert in alerts:
                print(" 🔴", alert)
    except Exception as e:
        print("⚠️ Lỗi khi xử lý dữ liệu:", e)

# Khởi tạo MQTT subscriber
client = mqtt.Client(client_id="hiot-detector")
client.username_pw_set(config.MQTT_USERNAME, config.MQTT_PASSWORD)

client.on_message = on_message

client.connect(MQTT_BROKER, MQTT_PORT)
client.connect(config.MQTT_BROKER, config.MQTT_PORT)

client.subscribe(f"{config.TOPIC_PREFIX}/#")

print(f"🔎 Detector đang lắng nghe topic `{MQTT_TOPIC}` ...")
client.loop_forever()

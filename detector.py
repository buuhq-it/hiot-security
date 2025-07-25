# detector.py
import time, json
from datetime import datetime

import paho.mqtt.client as mqtt
import config

from security_detector import rules

def publish_alert(client, device_id, alert_type, message):
    alert_payload = {
        "device_id": device_id,
        "alert_type": alert_type,
        "message": message,
        "timestamp": time.time()
    }
    client.publish(f"{config.TOPIC_PREFIX}/detector", json.dumps(alert_payload))
    
# Hàm khi nhận tin nhắn
def on_message(client, userdata, msg):
    try:
        payload = json.loads(msg.payload.decode())
        alerts = rules.check_rules(payload)

        if alerts:
            print(f"[{datetime.now().isoformat()}] 📣 PHÁT HIỆN BẤT THƯỜNG:")
            for alert in alerts:
                print(" 🔴", alert)
                publish_alert(client, payload.get("device_id", "unknown"), "SECURITY_ALERT", alert)
    except Exception as e:
        print("⚠️ Lỗi khi xử lý dữ liệu:", e)

# Khởi tạo MQTT subscriber
client = mqtt.Client(client_id="hiot-detector")
client.username_pw_set(config.MQTT_USERNAME, config.MQTT_PASSWORD)

client.on_message = on_message

# client.connect(MQTT_BROKER, MQTT_PORT)
client.connect(config.MQTT_BROKER, config.MQTT_PORT)

client.subscribe(f"{config.TOPIC_PREFIX}/#")

print(f"🔎 Detector đang lắng nghe topic {config.TOPIC_PREFIX}/# ...")
client.loop_forever()

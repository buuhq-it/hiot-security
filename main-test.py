import paho.mqtt.client as mqtt
import json

# Cấu hình kết nối MQTT
broker = "mqtt.technote.online"
port = 1883  # hoặc 9001 nếu dùng websocket
username = "iot"
password = "Password123"
topic = "paper_wifi/test/"

# Payload dữ liệu
payload = {
    "humidity": 25,
    "temperature": 12,
    "battery_voltage_mv": 5555
}

# Khởi tạo client và cấu hình xác thực
client = mqtt.Client(client_id="python-hiot-sender")
client.username_pw_set(username, password)

# Kết nối và gửi dữ liệu
try:
    client.connect(broker, port, keepalive=60)
    client.publish(topic, json.dumps(payload), qos=0)
    print("Đã gửi dữ liệu thành công.")
    client.disconnect()
except Exception as e:
    print(f"Lỗi khi gửi dữ liệu: {e}")

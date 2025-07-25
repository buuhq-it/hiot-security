# rules.py

VALID_MACS = {"A1:B2:C3:D4:E5:F6", "A2:B3:C4:D5:E6:F7", "A3:B4:C5:D6:E7:F8", "A4:B5:C6:D7:E8:F9"}

def check_rules(payload):
    alerts = []

    device_id = payload.get("device_id")
    mac = payload.get("mac_address")
    heart_rate = payload.get("heart_rate")
    temperature = payload.get("temperature")

    if mac and mac not in VALID_MACS:
        alerts.append(f"[{device_id}] MAC address bất thường: {mac}")

    if heart_rate and heart_rate > 160:
        alerts.append(f"[{device_id}] Nhịp tim quá cao: {heart_rate} bpm")

    if temperature and (temperature > 39 or temperature < 35):
        alerts.append(f"[{device_id}] Nhiệt độ bất thường: {temperature}°C")

    return alerts

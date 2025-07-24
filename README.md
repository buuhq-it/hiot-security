# hiot secure

sudo docker container exec mosquitto mosquitto_pub \
  -t 'paper_wifi/test/' \
  -m '{"humidity":25, "temperature":28, "battery_voltage_mv":3060}' \
  -u iot \
  -P Password123

  python3 -m venv venv-hiot
pip install paho-mqtt

source venv-hiot/bin/activate

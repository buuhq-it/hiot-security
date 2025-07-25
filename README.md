# hiot secure

sudo docker container exec mosquitto mosquitto_pub \
  -t 'paper_wifi/test/' \
  -m '{"humidity":25, "temperature":28, "battery_voltage_mv":3060}' \
  -u iot \
  -P Password123

  python3 -m venv venv-hiot
pip install paho-mqtt

source venv-hiot/bin/activate

```text
from(bucket: "some_data")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) =>
    r.device_id == "watch-001" and
    r._field == "heart_rate"
  )

from(bucket: "some_data")
|> range(start: v.timeRangeStart, stop: v.timeRangeStop)
|> filter(fn: (r) =>
  r.device_id == "home-001" and
  r._field == "temperature"
)

from(bucket: "some_data")
|> range(start: v.timeRangeStart, stop: v.timeRangeStop)
|> filter(fn: (r) =>
  r.device_id == "elder-001" and
  r._field == "fall_detected"
)

from(bucket: "some_data")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) =>
    r.device_id == "elder-001" and
    (r._field == "gps_location.lat" or r._field == "gps_location.lon")
  )

latData = from(bucket: "some_data")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) =>
    r.device_id == "elder-001" and
    r._field == "gps_location_lat"
  )

lonData = from(bucket: "some_data")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) =>
    r.device_id == "elder-001" and
    r._field == "gps_location_lon"
  )

join(
  tables: {lat: latData, lon: lonData},
  on: ["_time", "device_id"]
)

from(bucket: "some_data")
|> range(start: v.timeRangeStart, stop: v.timeRangeStop)
|> filter(fn: (r) =>
  r.device_id == "cam-001" and
  r._field == "motion_detected"
)


from(bucket: "some_data")
  |> range(start: v.timeRangeStart, stop: v.timeRangeStop)
  |> filter(fn: (r) => r.topic == "iot/secure/detector")
  |> pivot(rowKey:["_time"], columnKey:["_field"], valueColumn:"_value")

```
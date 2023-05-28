import paho.mqtt.client as mqtt

hostname = "test.mosquitto.org"  # Sandbox broker
port = 1883  # Default port for unencrypted MQTT

topic = "PC000/#"  # Wildcard character '#' indicates all sub-topics (e.g. PC000/test, PC000/sensor/temperature, etc.)

def on_connect(client, userdata, flags, rc):
   # Successful connection is '0'
   print("[MQTT] Connection result: " + str(rc))

def on_publish(client, userdata, mid):
   print("[MQTT] Sent: " + str(mid))

def on_disconnect(client, userdata, rc):
   if rc != 0:
       print("[MQTT] Disconnected unexpectedly")

mqttc = mqtt.Client()
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_disconnect = on_disconnect
mqttc.connect(hostname, port=port)
mqttc.loop_forever()

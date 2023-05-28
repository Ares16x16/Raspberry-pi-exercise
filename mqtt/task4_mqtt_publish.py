import paho.mqtt.client as mqtt
hostname = "test.mosquitto.org"
port = 1883
topic_state = "PC000/traffic_light/emergency"
mqttc = mqtt.Client()

c = True

mqttc.publish(topic_state,emergency_status,qos=0,retain=False)
import paho.mqtt.publish as publish

hostname = "test.mosquitto.org"  # Sandbox broker
port = 1883  # Default port for unencrypted MQTT

topic = "PC000/test"  # '/' is used as the delimiter for sub-topics

publish.single(topic, payload="Hello, MQTT!", qos=0,
	hostname=hostname,
	port=port)

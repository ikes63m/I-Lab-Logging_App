import time
import paho.mqtt.client as mqtt


broker_address = "mqtt.example.com"
broker_port = 1883
username = "your_username"
password = "your_password"


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT broker")
        client.subscribe("connection/status")
        client.subscribe("network/health")
    else:
        print("Connection failed")

def on_message(client, userdata, msg):
    topic = msg.topic
    payload = msg.payload.decode()
    print(f"Received message: {topic} - {payload}")

    # Log the information or take appropriate action based on the topic and payload

def on_disconnect(client, userdata, rc):
    print("Disconnected from MQTT broker")
client = mqtt.Client()
client.username_pw_set(username, password)
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

client.connect(broker_address, broker_port, keepalive=60)
client.loop_start()

while True:
    time.sleep(1)
# Publish network connection status
client.publish("connection/status", "connected")

# Publish network health status
client.publish("network/health", "good")


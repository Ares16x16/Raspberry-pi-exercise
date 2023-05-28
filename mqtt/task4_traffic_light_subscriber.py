import RPi.GPIO as GPIO
import time
import random
import threading
import paho.mqtt.client as mqtt

hostname = "test.mosquitto.org"  # Sandbox broker
port = 1883  # Default port for unencrypted MQTT
topic = "PC000/#"
status = False
def on_connect(client, userdata, flags, rc):
   # Successful connection is '0'
   print("[MQTT] Connection result: " + str(rc))

def on_publish(client, userdata, mid):
   print("[MQTT] Sent: " + str(mid))
   status = mid

def on_disconnect(client, userdata, rc):
   if rc != 0:
       print("[MQTT] Disconnected unexpectedly")

# Initialize client instance
client = mqtt.Client()

# Bind events to functions
client.on_connect = on_connect
client.on_message = on_message
client.on_disconnect = on_disconnect

# Connect to the specified broker
client.connect(hostname, port=port)


GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

left_button = 10
red = 7
green = 24
GPIO.setup(left_button, GPIO.IN, GPIO.PUD_UP)

GPIO.setup(red, GPIO.OUT)
GPIO.setup(green, GPIO.OUT)

# Define a function to control both the Red and Green LEDs
def light_on(red_on, green_on):
    

    if red_on == 1:
        GPIO.output(red, 1)
    if green_on == 1:
        GPIO.output(green, 1)
    if red_on == 0:
        GPIO.output(red, 0)
    if green_on == 0:
        GPIO.output(green, 0)

def control_time():
    light_on(0,1)
    time.sleep(5)
    light_on(0,0)
    time.sleep(0.5)
    light_on(0,1)
    time.sleep(0.5)
    light_on(0,0)
    time.sleep(0.5)
    light_on(0,1)
    time.sleep(0.5)
    light_on(0,0)
    time.sleep(0.5)
    light_on(0,1)
    time.sleep(0.5)
    light_on(1,0)



# Define a new subclass of the default Thread class
class buttonThread (threading.Thread):
    # Override the __init__() method if you want to add more arguments
    def __init__(self, threadID, name):
        threading.Thread.__init__(self)
        self.threadID = threadID
        self.name = name

    # Override the run() method to implement the thread behavior
    def run(self):
        print ('Starting ' + self.name + ' for button detection.')
        try:
            while True:
                if status:
                    break
                mqttc.publish(topic_state,1,qos=0,retain=False)  # State 1
                control_time()
                
                time_green = time.time()
                button_hold_pass = False
                
                mqttc.publish(topic_state,2,qos=0,retain=False)  # State 2
                
                while (GPIO.input(left_button)==True):
                    # do nth!
                    pass
                if status:
                    break        
                if GPIO.input(left_button)==False:
                    #Record the start time
                    while (button_hold_pass==False):
                        start_time = time.time()
                        while(GPIO.input(left_button)==False):
                            #Record the end time
                            end_time = time.time()
                            pass
                        interval = end_time - start_time
                        print('Left button pressed for ', interval)
                        if status:
                            break
                        if (interval >= 0.5):
                            button_hold_pass = True
                            
                            
                    if (interval >= 0.5):
                        current_time = time.time()
                        if (current_time - time_green >= 5):
                            mqttc.publish(topic_state,3,qos=0,retain=False)  # State 3
                            if status:
                                break
                            time.sleep(3)
                            continue
                        elif (current_time - time_green < 5):
                            while (current_time - time_green < 5):
                                current_time = time.time()
                            mqttc.publish(topic_state,3,qos=0,retain=False) # State 3
                            if status:
                                break
                            time.sleep(3)
                            continue
                if status:
                    break
                print('Left button pressed for ', interval)
            while status:
                light_on(1,0)
                time.sleep(0.5)
                light_on(0,0)
                time.sleep(0.5)
        except KeyboardInterrupt:
            print('Thread Exception.')
        finally:
            print("Cleaning up GPIO...")
            GPIO.cleanup()

if __name__ == '__main__':
   # Inside main thread
   
   # Create an instance of the Thread subclass you have just created
   thread1 = buttonThread(1, "Thread-1")

   # Daemon threads will be stopped when the main program is terminated
   # This must be set before calling the start() method!!
   thread1.daemon = True

   # Start a new thread by invoking start(), then the run() method will be called
   thread1.start()


import RPi.GPIO as GPIO
import time
import random
import threading

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
                control_time()
                time_green = time.time()
                button_hold_pass = False
                
                while (GPIO.input(left_button)==True):
                    # do nth!
                    pass
                        
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
                        if (interval >= 0.5):
                            button_hold_pass = True
                            
                    if (interval >= 0.5):
                        current_time = time.time()
                        if (current_time - time_green >= 5):
                            time.sleep(3)
                            continue
                        elif (current_time - time_green < 5):
                            while (current_time - time_green < 5):
                                current_time = time.time()
                            time.sleep(3)
                            continue
                print('Left button pressed for ', interval)
        except :
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


from sense_hat import SenseHat
import datetime
from time import sleep
sense = SenseHat()
sense.clear()

"""
pressure = sense.get_pressure()
print(pressure)
    
humidity = sense.get_humidity()
print(humidity)
"""

f = open('record.txt', 'w')
for i in range(50):
    temp = sense.get_temperature()
    line = str(datetime.datetime.now()) + '  ' + str(round(temp,2))
    f.write(line + '\n')
    sleep(1)
    print('ionserting line:' + str(i))
f.close()

print('Done')



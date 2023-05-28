from sense_hat import SenseHat

sense = SenseHat()
sense.clear()

pressure = sense.get_pressure()
print(pressure)
    
humidity = sense.get_humidity()
print(humidity)


def temp(event):
    if event.action == 'pressed':       
        temp = sense.get_temperature()
        print(round(temp,2))

sense.stick.direction_any = temp






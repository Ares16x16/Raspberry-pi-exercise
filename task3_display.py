from sense_hat import SenseHat
import random

sense = SenseHat()

blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255,0,0)
orange = (255,127,0)
green = (0,255,0)
indigo = (75, 0 ,130)
violet = (155,38,182)
white = (255,255,255)

colour = (blue, yellow, red, orange, green, indigo, violet, white)


while True:
  sense.show_message("EEE is awesome!", text_colour=colour[random.randrange(8)], back_colour=colour[random.randrange(8)], scroll_speed=0.05)
  

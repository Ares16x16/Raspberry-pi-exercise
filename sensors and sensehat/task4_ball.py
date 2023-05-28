from sense_hat import SenseHat
from time import sleep
import random
sense = SenseHat()

ball_position = [3, 3] # coordinates of the starting position
x = 0
y = 0
white = (255, 255, 255)
flag = False
blue = (0, 0, 255)
yellow = (255, 255, 0)
red = (255,0,0)
orange = (255,127,0)
green = (0,255,0)
indigo = (75, 0 ,130)
violet = (155,38,182)
colour = (blue, yellow, red, orange, green, indigo, violet, white)
sense.set_pixel(ball_position[0], ball_position[1], white)

while True:
  sleep(1)	# sleep for 1 second
  if (ball_position[0] == 0):
    ball_position[0] += 1
    flag = True
  if (ball_position[0] == 7):
    ball_position[0] -= 1
    flag = True
  if (ball_position[1] == 0):
    ball_position[1] += 1
    flag = True
  if (ball_position[1] == 7):
    ball_position[1] -= 1
    flag = True
  if (flag == False and ball_position[0] != 0 and ball_position[0] != 7 and ball_position[1] != 0 and ball_position[1] != 7):
    x = random.randint(-1, 1)
    y = random.randint(-1, 1)
    if (x == 0 and y == 0):
      x = 1
    ball_position[0] += x  # generate a new x-position
    ball_position[1] += y# generate a new y-position
  flag = False
  sense.clear()
  sense.set_pixel(ball_position[0], ball_position[1], colour[random.randrange(8)])

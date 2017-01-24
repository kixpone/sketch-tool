from pymouse import PyMouse
from pykeyboard import PyKeyboard
import random
import time

### User settings. Mess around with these!
watch_time = 60
draw_time = 60

click_position = [100, 200]# I'd like to make it so you can click to
                          # set the position on the pause button, but
                          # that requires more code yet.
click = True     #If true tool will click the screen
spacebar = False #If true tool will press spacebar

### Not user settings. Mess around with these at your own risk!
click_args = click_position + [1]
m = PyMouse()
k = PyKeyboard()
#x_dim,y_dim = m.screen_size()
#x_dim/2, y_dim/2, # would be middle of screen

def what_episode():
  s=random.randint(1,6)
  e=random.randint(1,26)
  return("se{}ep{}".format(s,e))

def click_function():
  m.click(*click_args)
def spacebar_function():
  k.tap_key(' ')

def watch():
  while True:
    time.sleep(watch_time)
    if click:
      click_function()
    if spacebar:
      spacebar_function()
    time.sleep(draw_time)
    m.click(*click_args)
      

if __name__=="__main__":
  print("Try watching:")
  print(what_episode())
  print("It's a good one!")
  print("You are set to watch {}s and then draw for {}s.".format(
            watch_time,draw_time))
  print("At that rate, a 20m episode will take you {}m.".format(
            str(int((float(watch_time+draw_time)
                  /watch_time) * 20))))
  print("Press 'Ctrl C' in this window when you're ready to stop.")
  print("Commencing clicking!")
  try:
    watch()
  except KeyboardInterrupt:
    print("\rSee you next time!")



import webbrowser
import time
import keyboard
#import pynput
#mouse = pynput.mouse.Controller()

#Imma sry Riley the moving the mouse don't work
#Try a different library

while True:
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1) #Spams the rickrolls
    if keyboard.is_pressed('r'): #ALT+F4 closes the current window but not the others so an overide is needed
        break
    #mouse.position = (0, 0)  # Move the mouse to (0,0) to disable clicks
    time.sleep(0.1)  # Add a small delay to avoid exploding CPU usage #Remove if you want utter chaos

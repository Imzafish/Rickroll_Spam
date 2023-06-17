import webbrowser
import time
import keyboard

while True:
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1)
    if keyboard.is_pressed('r'):
        break
exit()

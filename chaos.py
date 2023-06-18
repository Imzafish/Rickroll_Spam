import webbrowser
import time
import keyboard

def disable_alt_f4(e):
    if e.event_type == keyboard.KEY_DOWN:
        if e.name == 'alt' and keyboard.is_pressed('f4'):
            return False  # Block the Alt+F4 combination

# Register the event handler to block Alt+F4
keyboard.hook(disable_alt_f4)

while True:
    webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ", new=1)
    if keyboard.is_pressed('r'):
        break
    time.sleep(0.1)

# Unregister the event handler when the loop ends
keyboard.unhook(disable_alt_f4)



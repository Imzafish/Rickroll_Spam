import webbrowser
import time
import keyboard
import ctypes
from pycaw.pycaw import AudioUtilities

# Get the default audio interface
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(ctypes.c_ulonglong(0), ctypes.IUnknown, None)

# Get the volume control
volume = interface.QueryInterface(ctypes.pointer(ctypes.c_float))

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
    volume.SetMasterVolumeLevel(0, None)  # Set volume to maximum (1.0)
    time.sleep(0.1)

# Unregister the event handler when the loop ends
keyboard.unhook(disable_alt_f4)
exit()


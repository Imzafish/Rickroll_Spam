from distutils.core import setup # Need this to handle modules
import py2exe 
import webbrowser # Now we need this to import the required methods/functions so the toexe can parse it!
import time
import keyboard
from pynput.mouse import Controller
from shutil import rmtree

try: # remove the temporary folders from last build bcos i don't know what will happen if they stay
    rmtree('dist/')
    rmtree('build/')
except:
    pass

try:
    setup(
        options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
        console = [{'script': "chaos.py"}],
        zipfile = None,
    )
except SystemExit:
    input('Please try to run toexe.bat as administrator, not this as a normal python file!\nPress enter to exit')

print('Now there should be a chaos.exe file in the dist folder! Check it out!')
if input('Press enter to exit or 1 to remove all the temporary junk we don\'t need') == '1':
    rmtree('dist/lib/')
    rmtree('build')
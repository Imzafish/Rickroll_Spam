from distutils.core import setup # Need this to handle modules
import py2exe 
import webbrowser # Now we need this to import the required methods/functions so the toexe can parse it!
import time
import keyboard
from pynput.mouse import Controller

print('If you are running this as the python file, don\'t. Run the toexe.bat file.')

setup(
    options = {'py2exe': {'bundle_files': 1, 'compressed': True}},
    console = [{'script': "chaos.py"}],
    zipfile = None,
)

#RIIIIIIILEY you have a problem to fix with this code! (Run toexe.bat)
#You can fix it this time!
#HINT: research everything
"""
error: Multiple top-level modules discovered in a flat-layout: ['chaos', 'toexe'].

To avoid accidental inclusion of unwanted files or directories,
setuptools will not proceed with this build.

If you are trying to create a single distribution with multiple modules
on purpose, you should not rely on automatic discovery.
Instead, consider the following options:

1. set up custom discovery (`find` directive with `include` or `exclude`)
2. use a `src-layout`
3. explicitly set `py_modules` or `packages` with a list of names

To find more information, look for "package discovery" on setuptools docs.
PS C:\Users\maxwe\Documents\GitHub\Rickroll_Spam> python toexe.py py2exe
If you are running this as the python file, don't. Run the toexe.bat file.
error: Multiple top-level modules discovered in a flat-layout: ['chaos', 'toexe'].

To avoid accidental inclusion of unwanted files or directories,
setuptools will not proceed with this build.

If you are trying to create a single distribution with multiple modules
on purpose, you should not rely on automatic discovery.
Instead, consider the following options:

1. set up custom discovery (`find` directive with `include` or `exclude`)
2. use a `src-layout`
3. explicitly set `py_modules` or `packages` with a list of names

To find more information, look for "package discovery" on setuptools docs."""
from distutils.core import setup # Need this to handle modules
import py2exe
from shutil import rmtree
import sys, os

packages = ['keyboard', 'time', 'webbrowser']

sys.argv.append('py2exe')

try: # remove the temporary folders from last build bcos i don't know what will happen if they stay
    rmtree('dist/')
    rmtree('build/')
except:
    pass

try:
    setup(
        name='Chaos',
        version='1.0',
        description='Do not run at all costs... unless you are dying of curiosity. Will not delete anything on your laptop.',
        options = {'py2exe': {"includes": packages,
                            "bundle_files": 1,
                            'compressed': True}},
        console = ["chaos.py"],
        zipfile = None,
    )
except SystemExit:
    input('Please try to run toexe.bat as administrator, not this as a normal python file!\nPress enter to exit')
    exit()

print('Now there should be a chaos.exe file in the dist folder! Check it out!')
if input('Press enter to exit or 1 to remove all the temporary junk we don\'t need') == '1':
    rmtree('dist/lib/')
    rmtree('build')
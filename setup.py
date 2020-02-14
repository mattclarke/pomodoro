from setuptools import setup

APP = ['pomodoro.py']
DATA_FILES = []
OPTIONS = {
    'argv_emulation': True,
    'iconfile': 'icon.icns',
    'plist': {
        'CFBundleShortVersionString': '0.2.0',
        'LSUIElement': True,
        'PyRuntimeLocations': [
                '/Users/mattclarke/miniconda3/lib/libpython3.7m.dylib'
               ]
    },
    'packages': ['rumps'],
}

setup(
    app=APP,
    name='Pomodoro',
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'], install_requires=['rumps']
)

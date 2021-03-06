"""
This is a setup.py script generated by py2applet

Usage:
    python setup.py py2app
"""

from setuptools import setup

APP = ['Studio One Import.py']
DATA_FILES = ['GUI.xib', 'util.py']
RESOURCES = [('studio_one_session_parser',
              ['studio_one_session_parser/song_model.py']),
             ('studio_one_session_parser/parsers',
              ['studio_one_session_parser/parsers/audio_mixer.py',
               'studio_one_session_parser/parsers/audio_synth_folder.py',
               'studio_one_session_parser/parsers/media_pool.py',
               'studio_one_session_parser/parsers/mixer_console.py',
               'studio_one_session_parser/parsers/music_track_device.py',
               'studio_one_session_parser/parsers/song.py',
               'studio_one_session_parser/parsers/song_parser.py'])]

DESCRIPTION = "A macOS app for importing Presonus Studio One session " \
              "data into a different session"

OPTIONS = {
    "resources": RESOURCES,
    "packages": ['lxml'],
    "frameworks": ['/usr/lib/libxml2.2.dylib'],
}

COMMON_OPTIONS = {
    'name': "Studio One Session Import",
    'version': "0.1",
    'description': DESCRIPTION,
}

setup(
    app=APP,
    data_files=DATA_FILES,
    options={'py2app': OPTIONS},
    setup_requires=['py2app'],
    **COMMON_OPTIONS
)

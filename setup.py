from setuptools import setup

setup(
    name='crackthecode',
    version='1.0.0',
    author='Najm Ajmal',
    description='A simple 4-digit Crack the Code Game',
    packages=['crackthecode'],
    entry_points={
        'console_scripts': [
            'crackthecode = crackthecode.game:play_game',
        ],
    },
)

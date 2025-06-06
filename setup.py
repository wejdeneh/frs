from setuptools import setup

setup(
    name='spiffs-tool',
    version='0.1',
    py_modules=['spiffs_forensics'],
    install_requires=[],
    entry_points={
        'console_scripts': [
            'spiffs-tool = spiffs_forensics:main',
        ],
    },
)
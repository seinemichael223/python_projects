from setuptools import setup

setup(
    name='fnccalc',
    version='1.0',
    py_modules=['fnccalc'],
    entry_points={
        'console_scripts': [
            'fnccalc=fnccalc:main',
        ],
    },
)

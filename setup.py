from setuptools import find_packages, setup


setup(
    name='Command Line Tutorial',
    version='1.0.0',
    entry_points={
        'console_scripts': [
            'hello=hey.tut1:say_hello',
            'howdy=hey.tut2:say_hello',
        ]
    },
    author='Peter McDonald',
    description='Quick tutorial showing how a command may work',
    long_description='Quick tutorial showing how a command may work',
    packages=find_packages(),
    package_dir={'hey': 'hey'},
)

from setuptools import setup

setup(
    name='EEg-Emotion-Recognition',
    version='0.0.1',
    description='Emotion recognition using EEG from DEAP Dataset',
    author='Thanyathorn Thanapattheerakul, folking from Raghav714 GitHub',
    author_email='th.thanyathorn@gmail.com',
    install_requires=[
        'numpy',
        'scipy',
        'pandas',
        'PyWavelets',
        'matplotlib',
        'sklearn'
    ]
)

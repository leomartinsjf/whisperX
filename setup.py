import os

import pkg_resources
from setuptools import setup, find_packages

setup(
    name="whisperx",
    py_modules=["whisperx"],
    version="3.1.1",
    description="Time-Accurate Automatic Speech Recognition using Whisper.",
    readme="README.md",
    python_requires=">=3.8",
    author="Max Bain",
    url="https://github.com/m-bain/whisperx",
    license="MIT",
    packages=find_packages(exclude=["tests*"]),
    install_requires=[
        str(r)
        for r in pkg_resources.parse_requirements(
            open(os.path.join(os.path.dirname(__file__), "requirements.txt"))
        )
    ] + ["pyannote.audio @ git+https://github.com/pyannote/pyannote-audio@ad8a9e9d405343c5a93ccc11b641d0a2e8842a0d"],
    entry_points = {
        'console_scripts': ['whisperx=whisperx.transcribe:cli'],
    },
    include_package_data=True,
    extras_require={'dev': ['pytest']},
)

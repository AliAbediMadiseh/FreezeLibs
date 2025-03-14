from setuptools import setup, find_packages

setup(
    name="FreezeLibs",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[],
    entry_points={
        "console_scripts": [
            "FreezeLibs=FreezeLibs.FreezeLibs:main",
        ],
    },
    description="A tool to extract and save Python library imports.",
    author="Ali Abedi Madiseh",
    author_email="your.email@example.com",
    url="https://github.com/AliAbediMadiseh/FreezeLibs",
)
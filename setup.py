from setuptools import setup, find_packages, Extension

setup(
    name="CDSMatch",
    version="1.0",
    packages=find_packages(),
    install_requires=[
        "biopython",
        "pyyaml==5.4.1",
        "pandas==2.2.3",
        "ace_tools_open==0.1.0"
    ],
    entry_points={
        "console_scripts": [
            "CDSMatch = CDSMatch.main:main",
        ],
    },
    python_requires='>=3.8',
)

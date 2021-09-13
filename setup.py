"""Setup file."""
import datetime
import glob
import os

import setuptools
from setuptools import setup

version = datetime.datetime.now().strftime("%Y%m%d")
with open("VERSION", "w") as version_file:
    version_file.write(version)

requirements = []
if os.path.exists("requirements.txt"):
    with open("requirements.txt") as f:
        requirements = f.read().splitlines()

scripts = glob.glob("bin/*.py")

data_files = glob.glob("data/*")
setup(
    name="elite-journey",
    maintainer="Shane Fagan",
    maintainer_email="shanepatrickfagan@gmail.com",
    version=version,
    packages=setuptools.find_packages(),
    scripts=scripts,
    python_requires=">3.9",
    data_files=[
        ("data/", data_files),
    ],
    install_requires=["pyyaml", "sqlalchemy", "requests"],
)

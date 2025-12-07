from setuptools import setup, find_packages

setup(
    name="simplemp",
    version="0.3.0",
    packages=find_packages(),
    include_package_data=True,
    author="S.M Sadat",
    author_email="smsadat788@gmail.com",
    install_requires = [
        "av>=16.0.1",
        "numpy>=2.3.5"
    ],
)
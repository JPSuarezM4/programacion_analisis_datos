from setuptools import setup, find_packages


setup(
    name="edu_pad",
    version="0.0.1",
    author="Juan Suarez Dev",
    author_email="juan.suarez@est.iudigital.edu.co",
    description="A package for educational purposes",
    py_modules=["actividad_1, actividad_2, actividad_3"],
    install_requires=[
        "pandas",
        "openpyxl",
        "requests",
        "beautifulsoup4",
    ],
)
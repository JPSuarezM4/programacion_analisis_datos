from setuptools import setup, find_packages


setup(
    name="edu_pad",
    version="0.0.1",
    author="Juan Suarez Dev",
    author_email="juan.suarez@est.iudigital.edu.co",
    description="A package for educational purposes",
    py_modules=["actividad_1, actividad_2"],
    install_requires=[
        "pandas>=2.0.0",
        "openpyxl>=3.1.0",
        "requests>=2.28.0",
        "beautifulsoup4>=4.12.0",
        "streamlit>=1.20.0",
        "ydata-profiling>=4.5.0,<4.7.0",  # Compatible con Python 3.11
        "plotly>=5.0.0",
        "streamlit-plotly-events",
        "streamlit-ace",
        "streamlit-option-menu",
        "streamlit-aggrid",
        "streamlit-extras",
    ],

)
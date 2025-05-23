FROM python:3.9-slim

WORKDIR /programacion_analisis_datos

COPY setup.py .

RUN pip install -e .

CMD [ "python","setup.py" ]
FROM python:3.9-slim

WORKDIR /programacion_analisis_datos

COPY . .

RUN mkdir -p static/csv static/db

RUN pip install --upgrade pip \
    && pip install -e . \
    && rm -rf /root/.cache/pip

ENV PYTHONPATH=/programacion_analisis_datos/src


ENTRYPOINT ["python", "-m"]


CMD ["edu_pad.main_extractor"]
ARG PYTHON_VERSION=3.10-slim

FROM python:${PYTHON_VERSION}

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir -p /code

WORKDIR /code

COPY requirements.txt /tmp/requirements.txt
RUN set -ex && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /root/.cache/
COPY . /code

ENV SECRET_KEY "E4yaoX10vryVOvfrLvIvFQpWtPi1Cv4FpuP7sOc9WXuWqOH4NR"
RUN python manage.py collectstatic --noinput

EXPOSE 8000

CMD ["python","manage.py","runserver","0.0.0.0:8000"]

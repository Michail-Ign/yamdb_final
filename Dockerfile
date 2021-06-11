FROM python:3.8.5

COPY . /code
WORKDIR /code
RUN pip install -r /code/requirements.txt
FROM python:3.7-slim-stretch


WORKDIR /app

COPY requirements.txt .
RUN pip3 install -r requirements.txt

COPY message_generator ./message_generator

ENTRYPOINT python3 message_generator/__main__.py
FROM python:3.8-slim-buster

RUN mkdir -p /app
WORKDIR /app

COPY requirements.txt ./
RUN pip install -r requirements.txt

COPY src .

ENV FLASK_APP=app/app.py

CMD ["flask", "run", "--host=0.0.0.0"]




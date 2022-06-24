FROM python:3.7-slim-buster

WORKDIR /app

COPY requirements.txt prepare.sh /app/

RUN pip3 install -r requirements.txt

RUN bash prepare.sh 

COPY . /app/

# Đã cd vào flask api

CMD [ "python3", "serve.py"]
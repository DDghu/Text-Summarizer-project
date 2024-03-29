# To create docker image we need to exeute this code 
FROM python:3.10-slim-buster

RUN apt update -y && apt install awscli -y
WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt
RUN pip install --upgrade accelerate
RUN pip install -y transformers accelerate
RUN pip install transformers accelerate

CMD [ "python3","app.py" ]
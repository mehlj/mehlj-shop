FROM python:3.9-rc-buster

WORKDIR /usr/src/app

ENV FLASK_DEBUG=1

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/* /usr/src/app/

CMD [ "python", "./main.py" ]

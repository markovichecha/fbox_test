FROM python:3.7

WORKDIR /usr/src/app

COPY funbox/ /usr/src/app/funbox
COPY tests/ /usr/src/app/tests
COPY requirements.txt /usr/src/app
COPY main.ini /usr/src/app
COPY start.sh /usr/src/app
RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["sh", "start.sh"]
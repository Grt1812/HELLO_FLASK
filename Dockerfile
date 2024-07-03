FROM HELLO_FLASK
RUN apt-get update -y && \ apt-get install -y python-dev
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
COPY ./app

CMD [ "python","app.py"]
FROM python:3.8

WORKDIR /server

ADD . /server

RUN pip3 install -r requirements.txt && \
    pip3 install .

CMD ["server"]

EXPOSE 8018

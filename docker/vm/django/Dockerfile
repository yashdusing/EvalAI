FROM python:3.6.5

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
ADD requirements/* /code/
RUN pip install -r prod.txt
RUN pip install -r dev.txt

ADD . /code

CMD ["sh", "/code/docker/vm/django/container-start.sh"]

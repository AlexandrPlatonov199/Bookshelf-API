FROM python:3.11

RUN mkdir /bookshelf

WORKDIR /bookshelf

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x /bookshelf/docker/*.sh
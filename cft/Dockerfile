FROM python:3.11

RUN mkdir /сае

WORKDIR /сае

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

RUN chmod a+x docker/*.sh
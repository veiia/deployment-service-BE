FROM python:3.10
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

RUN mkdir /deployment
WORKDIR /deployment

COPY requirements requirements

RUN python -m pip install --upgrade pip
RUN pip3 install -r /deployment/requirements/base.txt

COPY . .
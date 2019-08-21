FROM python:3.6.7-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add bash && apk add nano
RUN mkdir /code
RUN mkdir /code/requirements
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
CMD exec gunicorn OwlsNest.wsgi_docker:application --bind 0.0.0.0:8005 --workers 3
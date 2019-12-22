FROM python:3.6.7-alpine
ENV PYTHONUNBUFFERED 1
RUN apk update && apk add bash && apk add nano
RUN mkdir /code
RUN mkdir /code/requirements
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/
RUN exec python manage.py collectstatic --settings=OwlsNest.settings-docker
CMD exec gunicorn OwlsNest.wsgi_docker:application --bind 0.0.0.0:8005 --workers 3

# build the image like this:
# docker build -t my_hiking:latest .

# run the container from 'shared', like this:
# docker run -d --name my_hiking --mount type=bind,source=/home/pi/shared,target=/shared -p 8005:8005 --restart always my_hiking:latest

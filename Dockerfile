FROM python:3.6.7-slim

ENV PYTHONUNBUFFERED 1
RUN apt-get update && apt-get install --no-install-recommends -y bash nano mc
RUN mkdir /src
WORKDIR /src
COPY . /src/

RUN pip install -r requirements.txt
RUN exec python manage.py collectstatic --settings=OwlsNest.settings-docker
CMD exec gunicorn OwlsNest.wsgi_docker:application --bind 0.0.0.0:8005 --workers 3

# build the image like this:
# docker build -t my_hiking:latest .

# run the container from 'shared', like this:
# docker run -d --name my_hiking --mount type=bind,source=$HOME/shared,target=/shared -p 8006:8005 --restart always my_hiking:latest

# log into the container
# docker exec -it my_hiking bash
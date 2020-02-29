FROM python:3.7
ADD . /srv/eye_tales
WORKDIR /srv/eye_tales
RUN apt update
RUN apt install -y vim
RUN pip install --upgrade pip
RUN pip3 install -r requirements.lock
CMD uwsgi --ini eye_tales.ini --wsgi-disable-file-wrapper
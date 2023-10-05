FROM python:3.10.9-buster

# for logging python during build
ENV PYTHONBUFFERED=1

# target folder on container
WORKDIR /code

# copy requirements.txt to target folder
COPY requirements.txt /code/

# install requirements
RUN pip install -r requirements.txt

# afterwards copy entire project
COPY . /code/

CMD gunicorn forumproject.wsgi --bind 0.0.0.0:8000 --workers=4

EXPOSE 8000

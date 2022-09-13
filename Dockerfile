#Pull base image
FROM python:3.9

#set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1


# Install django dependencies
RUN pip install --upgrade pip
COPY requirements.txt /payed/
RUN pip install -r /payed/requirements.txt

#work directory
WORKDIR /payed/src

#install npm dependencies 
RUN apt-get update && apt-get upgrade -y && \
    apt-get install -y nodejs \
    npm  

COPY src/package*.json ./
RUN npm install

# Copy project
COPY . /payed/

#run webpack
COPY src/webpack.common.js /payed/src/
COPY src/webpack.prod.js /payed/src/

RUN npm run build
CMD gunicorn --bind 0.0.0.0:$PORT core.wsgi



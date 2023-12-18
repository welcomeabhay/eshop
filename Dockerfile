#base image
From python:3.9

#set environment variable
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#set work directory
RUN mkdir /DockerHome

#where your code lives
WORKDIR /DockerHome



#install dependencies
RUN pip install --upgrade pip

ADD requirement.txt . 
RUN pip install -r requirement.txt 

# copy project
ADD ./ /DockerHome/

CMD ["python","manage.py","runserver"]

#port for the app
EXPOSE 8000

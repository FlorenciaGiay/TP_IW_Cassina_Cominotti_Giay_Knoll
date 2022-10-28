# syntax=docker/dockerfile:1

# The first instruction is what image we want to base our container on
# We Use an official Python runtime as a parent image
FROM python:3.8.10

# The enviroment variable ensures that the python output is set straight
# to the terminal with out buffering it first
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# create root directory for our project in the container
RUN mkdir /app_grupo1

# Set the working directory to /app_grupo1
WORKDIR /app_grupo1

COPY requirements.txt /app_grupo1/

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

# Copy the current directory contents into the container at /rafaelaemprende_service
COPY . /app_grupo1/

ENV SECRET_KEY="my_secret_key"
ENV DEBUG_VALUE=True
ENV EMAIL_HOST="smtp.gmail.com"
ENV EMAIL_HOST_USER="your.email@gmail.com"
ENV EMAIL_HOST_PASSWORD="your_password"
ENV EMAIL_PORT=587
ENV EMAIL_USE_TLS=True
ENV NUMBER_OF_ATTEMPTS_TO_CREATE_ENTREPRENEUR_PROFILE=3
ENV USE_S3="FALSE"

RUN mkdir -p /app_grupo1/data
RUN mkdir -p /app_grupo1/media

# If you want to execute a bash to run multiple things
# CMD ["/bin/bash","-c","./docker-startup.sh"]
CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000"]

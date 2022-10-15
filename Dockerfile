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

ENV RUNNING_IN_DOCKER = True

RUN mkdir -p /app_grupo1/data

# CMD ["python", "manage.py", "migrate", "&&", "python", "manage.py", "rebuild_index", "&&", "python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["/bin/bash","-c","./docker-startup.sh"]

# ---------------------------------------------------------------------

# # syntax=docker/dockerfile:1

# # The first instruction is what image we want to base our container on
# # We Use an official Python runtime as a parent image
# FROM python:3.8.10

# # The enviroment variable ensures that the python output is set straight
# # to the terminal with out buffering it first
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # create root directory for our project in the container
# RUN mkdir /rafaelaemprende_service

# # Set the working directory to /rafaelaemprende_service
# WORKDIR /rafaelaemprende_service

# # Copy the current directory contents into the container at /rafaelaemprende_service
# ADD . /rafaelaemprende_service/

# # Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

# ---------------------------------------------------------------------

# # syntax=docker/dockerfile:1

# # The first instruction is what image we want to base our container on
# # We Use an official Python runtime as a parent image
# FROM python:3.8.10

# # The enviroment variable ensures that the python output is set straight
# # to the terminal with out buffering it first
# ENV PYTHONDONTWRITEBYTECODE=1
# ENV PYTHONUNBUFFERED=1

# # Set the working directory to /rafaelaemprende_service
# WORKDIR /rafaelaemprende_service

# # Copy the current directory contents into the container at /rafaelaemprende_service
# COPY requirements.txt /rafaelaemprende_service/
# COPY media /rafaelaemprende_service/

# # Install any needed packages specified in requirements.txt
# RUN pip install -r requirements.txt

# COPY . /rafaelaemprende_service/
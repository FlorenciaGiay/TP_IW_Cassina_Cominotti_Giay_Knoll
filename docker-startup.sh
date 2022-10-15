#!/bin/bash

# Collect static files
echo ""
echo "##########################################################################"
echo "########################## Collect static files ##########################"
echo "##########################################################################"
python manage.py collectstatic --noinput

# Apply database migrations
echo ""
echo "##########################################################################"
echo "####################### Apply database migrations ########################"
echo "##########################################################################"
python manage.py migrate

# Uncomment this lines if you want to create a superuser automatically
# Create superuser
# echo ""
# echo "##########################################################################"
# echo "########################### Create a Superuser ###########################"
# echo "##########################################################################"
# DJANGO_SUPERUSER_USERNAME="admin2" \
# DJANGO_SUPERUSER_PASSWORD="ucse#admin#2022" \
# DJANGO_SUPERUSER_EMAIL="admin2@admin.com" \

# echo "DJANGO_SUPERUSER_USERNAME: " $DJANGO_SUPERUSER_USERNAME
# echo "DJANGO_SUPERUSER_PASSWORD: " $DJANGO_SUPERUSER_PASSWORD
# echo "DJANGO_SUPERUSER_EMAIL: " $DJANGO_SUPERUSER_EMAIL
# python manage.py createsuperuser --username $DJANGO_SUPERUSER_USERNAME --email $DJANGO_SUPERUSER_EMAIL --noinput

# Delete all indexes and update them
echo ""
echo "##########################################################################"
echo "################### Delete all indexes and update them ###################"
echo "##########################################################################"
python manage.py update_index --remove

# Start server
echo ""
echo "##########################################################################"
echo "############################ Starting server #############################"
echo "##########################################################################"
python manage.py runserver 0.0.0.0:8000
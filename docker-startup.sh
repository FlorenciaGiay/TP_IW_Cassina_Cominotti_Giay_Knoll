#!/bin/bash

# Collect static files
echo "##########################################################################"
echo "########################## Collect static files ##########################"
echo "##########################################################################"
python manage.py collectstatic --noinput

# Apply database migrations
echo "##########################################################################"
echo "####################### Apply database migrations ########################"
echo "##########################################################################"
python manage.py migrate

# Create superuser
echo "##########################################################################"
echo "########################### Create a Superuser ###########################"
echo "##########################################################################"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin2', 'admin2@admin.com', 'ucse$admin$2022')" | python manage.py shell

# Delete all indexes and update them
echo "##########################################################################"
echo "################### Delete all indexes and update them ###################"
echo "##########################################################################"
python manage.py update_index --remove

# Start server
echo "##########################################################################"
echo "############################ Starting server #############################"
echo "##########################################################################"
python manage.py runserver 0.0.0.0:8000
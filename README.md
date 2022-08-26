<p align="center">
  <a href="https://rafaela-emprende.herokuapp.com/" target="blank">
  <img src="https://rafaela-emprende-files-prod.s3.us-east-1.amazonaws.com/images/logo/Rafaela_Emprende_Logo.gif?response-content-disposition=inline&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF4aCXNhLWVhc3QtMSJGMEQCIAWev5ZsyyjWQhLN%2BSzYkP8a%2F6BoJN98LgW0vjoHkNeUAiB3UId31mCMsUvZxQcMZtAFWmQpdVIVgSOAAmOGBcRVnSrtAgjX%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDI0NjkyMDA1MjYzMSIMbjoxJlyfNv1Xf3pIKsECLqrqwNu6p4O6wSKPcvXwbUMEJWu7qB4xKYNKe8Zt3rrUx2KAtR4sYUs1TuRHgqhs1EjWomC6vzQEVgPncwmUnh1a5m7wFpEs0ljICivW9NKwAmlyiFDIYewmH%2BwTx1HcRrldWMS7dTHR5LLLK1Fh7plUzvDS7ROmG8nxmWOsvOxqyKgYDHD5AEun1f%2B4aWlaLrxfa3jlmLwoLz3GSHf7u8gBGqYvuqjTEPrPU54gc5x7IzhujWKT5kzr8uG6KH9YvuDhFIFTbHrz7PUB8l76RwLYECbsUBWaDu8TBVlwrCDieS%2Bg6aYq%2FfWVRMtHOVfBUA439KTSQuEV59kBW3bAQ7YCzmXmkNfjFTVOoTRaLM6OOyuAbE4klkHSiplWryPQXwDfOtTASQ5q1gk55eVvgYA1fyZIa6ay94tA9Y4IrGUnMPyPo5gGOrQC8FqbGhDupPcitW2B%2FBsrXaBiV00j1yIYrepR1rACGpwyE5%2FjjS%2BttIBul0%2Fbc2EhHTu%2BbMy850Q4iOEZLTvFozDZtUutbuTMKU%2B6RAYxOt9oJ1jzEw40qD6POe5WA%2BylhA7eIMdAqeqKrGcg0n2FweZ30oT%2FRnlxZnZTZf475zm5c0w56uV7yuCpLFqv%2BQaOlPgcBpb6KHXX2xbw%2F8nUqRDH3QWr7UmexllSlHWSJ7n%2B62ffpNtqt5a166cFVYQltkeJ%2FLF2HiUItX14O49aRoWTErfF2i49lM%2BCc%2BxzhTxye3vAYvz6r8SwG9mBKlXTVmxpzOfscPdm%2B03babSku4ayLZeh93iYkMz8R9x6du450bYgy2xefwSnp5IPMHpDSAbCnvbpBiX2o6G%2BIrmVlKGO7Do%3D&X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Date=20220826T134107Z&X-Amz-SignedHeaders=host&X-Amz-Expires=300&X-Amz-Credential=ASIATS7MU76LR3UXIKEE%2F20220826%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Signature=3695e7a57ed734b22edd9ba334acfeb465ef1ae59f4265ec4bb1ab22975fcbec" 
    width="120" 
    alt="Rafaela Emprende Logo" 
    style="border-radius:50%; width:30%"/>
  </a>
</p>

## Repositorio para el desarrollo del Trabajo Práctico de la materia Ingeniería Web.
### Integrantes del equipo:
##### * Paula Cassina
##### * Mauro Cominotti
##### * Florencia Giay
##### * Gonzalo Knoll

<br />
<br />

Éste es un Trabajo basado en la materia de Ingeniería Web de la UCSE. Link a la wiki de la materia: https://github.com/ucseiw-team/catedra/wiki

## Steps to clone this repository with Conda
El modelo de datos de ésta App es el siguiente:
<p align="center">
  <img src="./rafaela_emprende_data_model.png" alt="Rafaela Emprende Logo" style="width:100%"/>
</p>

<br />
<br />

## Steps to clone this repository with Conda
1. Clone this Django application with the optional step of creating a virtual environment.
```console
$ git clone https://github.com/FlorenciaGiay/TP_IW_Cassina_Cominotti_Giay_Knoll.git

$ cd TP_IW_Cassina_Cominotti_Giay_Knoll

$ conda create -n rafaela_emprende python=3.8

$ source activate rafaela_emprende
```

2. Install your requirements:
```console
$ pip install -r requirements.txt
```

3. Make your migrations:
```console
$ python manage.py makemigrations

$ python manage.py migrate
```

Should print:
```console
$ python manage.py makemigrations
No changes detected

$ python manage.py migrate
Operations to perform:
  Apply all migrations: admin, auth, contenttypes, sessions
Running migrations:
  Applying contenttypes.0001_initial... OK
  Applying auth.0001_initial... OK
  Applying admin.0001_initial... OK
  Applying admin.0002_logentry_remove_auto_add... OK
  Applying admin.0003_logentry_add_action_flag_choices... OK
  Applying contenttypes.0002_remove_content_type_name... OK
  Applying auth.0002_alter_permission_name_max_length... OK
  Applying auth.0003_alter_user_email_max_length... OK
  Applying auth.0004_alter_user_username_opts... OK
  Applying auth.0005_alter_user_last_login_null... OK
  Applying auth.0006_require_contenttypes_0002... OK
  Applying auth.0007_alter_validators_add_error_messages... OK
  Applying auth.0008_alter_user_username_max_length... OK
  Applying auth.0009_alter_user_last_name_max_length... OK
  Applying auth.0010_alter_group_name_max_length... OK
  Applying auth.0011_update_proxy_permissions... OK
  Applying auth.0012_alter_user_first_name_max_length... OK
  Applying sessions.0001_initial... OK
```

4. Create a new superuser
```console
$ python manage.py createsuperuser
```

Then you should see something like this:
```console
Username (leave blank to use 'mauro'): admin
Email address: admin@admin.com
Password: ucse$admin$2022
Password (again): ucse$admin$2022
Superuser created successfully.
```

5. Final checks
```console 
$ python manage.py runserver
```
Then the result should be something like this: 
```console 
$ python manage.py runserver
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
August 18, 2022 - 22:59:54
Django version 4.1, using settings 'rafaela_emprende.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

Open the browser to the local server IP  http://localhost:8000 or http://127.0.0.1:8000/


<br />
<br />

## Steps to Create a Django App (Condensed)
1. Creating a Django application starts with the optional step of creating a virtual environment.
```console
$ conda create -n <PROJECT_NAME> python=3.8

$ source activate <PROJECT_NAME>
```

2. Install Django: 
```console
$ pip install Django

# or

$ conda install -c anaconda django
```

3. Create a project in Django: 
```console
$ django-admin startproject <PROJECT_NAME>

# Or if you want to create it in the same directory:
# $ django-admin startproject <PROJECT_NAME> .
```

4. Create a Django App: 
```console
$ cd <PROJECT_NAME> 

# then

$ python manage.py startapp <APP_NAME>
```

5. Add app to settings.py: 
```python 
<PROJECT_NAME>/<PROJECT_NAME>/settings.py
```

6. Add URL to the APP in the project: 
```python 
<PROJECT_NAME>/<PROJECT_NAME>/urls.py
```

7. Create the APP urls.py file: 
```console
$ cd django_app then $ touch urls.py
```

8. Add a path to the Index in the URL patterns in 
```python 
<app_name>/urls.py.
```

9. Create the Index Route in 
```python 
<app_name>/views.py
```

10. Create the index.html template: 
```console
$ mkdir -p templates/<APP_NAME> 
```
```console
$ touch templates/<APP_NAME>/index.html
```
then add the HTML to the file.

11. Make the migrations: 
```console
$ cd .. 

# then

$ python manage.py migrate
```

12. Run the Django server: 
```console
$ python manage.py runserver 
```
Then open the browser to the local server IP (generally http://localhost:8000).

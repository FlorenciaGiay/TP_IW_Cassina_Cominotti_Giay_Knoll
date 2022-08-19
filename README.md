## Repositorio para el desarrollo del Trabajo Práctico de la materia Ingeniería Web.
### Integrantes del equipo:
##### * Paula Cassina
##### * Mauro Cominotti
##### * Florencia Giay
##### * Gonzalo Knoll

<br />
<br />

## Steps to clone this repository with Conda
1. Clone this Django application with the optional step of creating a virtual environment.
```console
$ git clone https://github.com/FlorenciaGiay/TP_IW_Cassina_Cominotti_Giay_Knoll.git
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
4. Create a new superuser
```console
$ python manage.py createsuperuser
```
5. Final checks
```console 
$ python manage.py runserver
```
Then open the browser to the local server IP (generally http://localhost:8000).


<br />
<br />

## Steps to Create a Django App (Condensed)
1. Creating a Django application starts with the optional step of creating a virtual environment.
```console
$ conda create -n rafaela_emprende python=3.8
$ conda activate rafaela_emprende
```
2. Install Django: 
```console
$ pip install Django
# or
$ conda install -c anaconda django
```
3. Create a project in Django: 
```console
$ django-admin startproject rafaela_emprende
```
4. Create a Django App: 
```console
$ cd rafaela_emprende 
# then
$ python manage.py startapp <APP_NAME>
```

5. Add app to settings.py: 
```python 
rafaela_emprende/rafaela_emprende/settings.py
```
6. Add URL to the APP in the project: 
```python 
rafaela_emprende/rafaela_emprende/urls.py
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

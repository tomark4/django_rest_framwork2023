1. Crear el entorno virtual

pipenv --python /usr/bin/python3

2. Activar el entorno virtual

pipenv shell

3. Instalar django

pip install django

4. Crear el proyecto de django

django-admin startproject <name_project> .

5. Arrancar el proyecto

python manage.py runserver

6. correr migraciones

python manage.py migrate

7. crear superuser

python manage.py createsuperuser

Visitar http://localhost:8000/

ready to work!

8. Crear nueva app

django-admin startapp <name_app>

9. Agregar la app en el fichero settings.py en el apartado installed_apps

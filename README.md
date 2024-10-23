# Requisitos previos
Asegúrate de tener Python instalado en tu sistema. Puedes descargarlo desde python.org.

## Instalación en MacOS
1.Clona este repositorio:

    git clone https://github.com/mrgomezsv/EDSChecklistProject.git
    
    cd smap_project_fazt_web

2.Crea y activa un entorno virtual (opcional pero recomendado):

    python3 -m venv venv
    source venv/bin/activate

3.Generar el Requirements

    pip freeze > requirements.txt


4.Instala las dependencias:

    pip install -r requirements.txt

    pip install asgiref==3.8.1
    pip install Django==5.1.2
    pip install djangorestframework==3.15.2
    pip install sqlparse==0.5.1

5.Crear una migración:

    python3 manage.py makemigrations
    
6.Correr todas las migraciones:

    python3 manage.py migrate

7.Asignación de la variable de ejecución del proyecto:

    python3 manage.py runserver


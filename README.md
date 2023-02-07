# Clothing Store with Django

The clothing store was built using the Django framework on Python language. To start, you need to enter SECRET_KEY any values in settings.py.

# Dependencies

Inside the virtual environment you will need to type in terminal this `pip install -r requirements.txt`

# Build service from Docker image

Requirements:

- Docker

## Run container and django:

Run this command in terminal in root derictory

- `docker-compose up -d --build `

Cd to the directory where the manage.py file is located and run the command:

- `py manage.py runserver`

App running on `http://127.0.0.1:8000/`

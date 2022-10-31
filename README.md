![image](Personal_Card_DRF.png)
# PERSONAL CARD REST API
Simple API with Django Rest Framework
## Requirements

- Python 3.9
- Django 4.1.2
- Django REST Framework 3.14.0

First, you need to clone the repository.

Once you have cloned the repository and want to create a virtual environment, you can do so by running the command.
```sh
python -m venv env
```
After this, it's necessary to activate the virtual environment.

You can install all the necessary dependencies with the command.
```sh
pip install -r requirements.txt
```

## Launch
>  How to run a project? 


First, you need to run the following command from the project root directory.

```sh
python manage.py migrate
```
> It will create a SQLite database in the project root directory.

To run the server, run the following command at the root of the project.
```sh
pip python manage.py runserver
```

Then open this URL in your browser.

```sh
http://127.0.0.1:8000/api/personal_cards/
```

## Description

The API supports two methods.
- GET
- POST

> GET

The GET method retrieves all cards (paginated by 10 card per page) from the database ordered by Last name, Name, Middle Name in ascending order.

> POST

The POST method accepts Personal Card information and adds it to a database table, if it does not exist.

Each record in the table also has a unique ID provided by the database.

## Testing

To test the app, run the following command.

```sh
python manage.py test
```
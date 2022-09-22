# Blood Levels
Django app that displays blood levels stored in a database and points out risk levels
(In Czech language)

## requires
- Python 3.9+
- Django 4.1.1+

## instructions for windows os
## install
- download the repo and unzip it
- set up and activate virtual environment
```python -m venv venv```
```venv\Scripts\activate.bat```
- import required libraries
```pip install -r requirements```
- set up your Django admin account
```python manage.py createsuperuser```
- run the server
```python manage.py runserver```

## use
In the browser:
- (optional) log into the admin interface
```http://127.0.0.1/admin```
- show the website
```http://127.0.0.1```

## notes
All records are stored in an SQLite database (```db.sqlite3```).
You can use a DB Browser for SQ Lite to browse the db contents.
Add/remove/replace records in the Django admin interface.
If a Tolerance field contains other chracter than '-', the level value
is highlighted by red color.

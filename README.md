# PythonFlaskLogin

## Flask-Login library with Flask-SQLAlchemy using werkzeug.security password hashing

- [Windows] - For Windows users

```sh
mkdir folder_name
cd folder_name
python -m venv auth
cd auth\Scripts
activate

You have all files in this repo So you don't need to run following example commands 
These are only for demonstration purposes 
How to create an empty file with desired extension in windows
(auth) C:\Users\your_name\Desktop\folder_name> pip install flask flask-sqlalchemy flask-login
(auth) C:\Users\your_name\Desktop\folder_name> mkdir project
(auth) C:\Users\your_name\Desktop\folder_name> cd project
(auth) C:\Users\your_name\Desktop\folder_name\project> type nul > __init__.py
(auth) C:\Users\your_name\Desktop\folder_name\project> type nul > main.py
(auth) C:\Users\your_name\Desktop\folder_name\project> type nul > auth.py
(auth) C:\Users\your_name\Desktop\folder_name\project> type nul > models.py
(auth) C:\Users\your_name\Desktop\folder_name> mkdir templates
(auth) C:\Users\your_name\Desktop\folder_name> cd templates
(auth) C:\Users\your_name\Desktop\folder_name\project\templates> type nul > base.html
(auth) C:\Users\your_name\Desktop\folder_name\project\templates> type nul > index.html
(auth) C:\Users\your_name\Desktop\folder_name\project\templates> type nul > login.html
(auth) C:\Users\your_name\Desktop\folder_name\project\templates> type nul > profile.html
(auth) C:\Users\your_name\Desktop\folder_name\project\templates> type nul > login.html
(auth) C:\Users\your_name\Desktop\folder_name\project\templates> type nul > signup.html

```

- [Unix] - For Unix users
```sh
mkdir folder_name
cd folder_name
python -m venv auth
auth/bin/activate
```

## Before you run flask don't forget to set 
```sh
for windows users
set FLASK_APP = project
set FLASK_DEBUG = 1

for unix users
export FLASK_APP = project
export FLASK_DEBUG = 1
```

## Flask run 
```sh
http://127.0.0.1:5000/
```


## Configuring the Database
- [REPL] - tell Flask-SQLAlchemy to create database in the Python-REPL
- Make sure that you have stopped the application and you are still in the virtual environment and in the current project folder not in the venv folder 
```python
from project import db, create_app
db.create_all(app=create_app())
```


![image](https://user-images.githubusercontent.com/24410504/116811212-b78aea80-ab50-11eb-9c99-f6495e77bc60.png)


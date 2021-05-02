# PythonFlaskLogin

## Flask-Login library with Flask-SQLAlchemy using werkzeug.security password hashing

- [Windows] - For Windows users

```sh
mkdir folder_name
cd folder_name
python -m venv auth
cd auth\Scripts
activate
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


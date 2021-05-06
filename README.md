[![Board Status](https://dev.azure.com/cgultekink/af207498-2d2c-48df-a062-54df34e8a2b3/20d01e07-adf2-4137-a9a1-cbcc276add1f/_apis/work/boardbadge/94f190f2-469c-4df3-82f8-5aa1e7477ab0)](https://dev.azure.com/cgultekink/af207498-2d2c-48df-a062-54df34e8a2b3/_boards/board/t/20d01e07-adf2-4137-a9a1-cbcc276add1f/Microsoft.RequirementCategory)
# PythonFlaskLogin

## _Flask-Login library with Flask-SQLAlchemy using werkzeug.security password hashing_

- [Windows] - For Windows users
Open your cmd and run these commands.

```sh
mkdir folder_name
cd folder_name
python -m venv auth
cd auth\Scripts
activate
(auth) C:\folder_name> pip install flask flask-sqlalchemy flask-login
(auth) C:\folder_name> mkdir project
(auth) C:\folder_name> cd project
```

You have all files in this repo So you don't need to run following example commands 
These are only for demonstration purposes 
How to create an empty file with desired extension in windows

```sh
for *.py files
(auth) C:\folder_name\project> type nul > __init__.py
(auth) C:\folder_name\project> type nul > main.py
(auth) C:\folder_name\project> type nul > auth.py
(auth) C:\folder_name\project> type nul > models.py

(auth) C:\folder_name\project> mkdir templates
(auth) C:\folder_name\project> cd templates

for *.html files
(auth) C:\folder_name\project\templates> type nul > base.html
(auth) C:\folder_name\project\templates> type nul > index.html
(auth) C:\folder_name\project\templates> type nul > login.html
(auth) C:\folder_name\project\templates> type nul > profile.html
(auth) C:\folder_name\project\templates> type nul > signup.html
```

```sh
then return back to folder_name
before you run flask don't forget to set FLASK_APP and FLASK_DEBUG
(auth) C:\folder_name> set FLASK_APP=project
(auth) C:\folder_name> set FLASK_DEBUG=1
(auth) C:\folder_name> flask run
```

- [Unix] - For Unix users
Open your Terminal and run these commands.

```sh
$ mkdir folder_name
$ cd folder_name
$ python -m venv auth
$ source auth/bin/activate
(auth)$ export FLASK_APP = project
(auth)$ export FLASK_DEBUG = 1
(auth)$ flask run
```


## Flask run 
```sh
* Debugger is active!
* Debugger PIN: SOMETHING
Running on http://127.0.0.1:5000/
```


## Configuring the Database
- [REPL] - tell Flask-SQLAlchemy to create database in the Python-REPL
- Make sure that you have stopped the application and you are still in the virtual environment and in the current project folder not in the venv folder 
```python
from project import db, create_app
db.create_all(app=create_app())
```


![image](https://user-images.githubusercontent.com/24410504/116811212-b78aea80-ab50-11eb-9c99-f6495e77bc60.png)


## License

MIT

**Free Software**

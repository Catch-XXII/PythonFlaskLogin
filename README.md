# PythonFlaskLogin
Flask-Login library with Flask-SQLAlchemy using werkzeug.security password hashing

mkdir any_folder_name
cd any_folder_name

install virtual env with following python code
python -m venv auth # [auth] can be any name which you desire

For 'Windows' users activate venv with following code
Go through cd auth\Scripts\ then run activate
C:\Users\your_name\Desktop\project_folder\auth\Scripts> only then activate

For 'Unix' system
source auth/bin/activate

###### Before you run Flask with 'flask run' command
do not forget to set FLASK_APP and FLASK_DEBUG 

###### For 'Windows' users
set FLASK_APP=project
set FLASK_DEBUG=1

###### For 'Unix' systems
export FLASK_APP=project
export FLASK_DEBUG=1

now you can run 
```flask run```

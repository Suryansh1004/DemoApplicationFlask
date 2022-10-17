# Flask Application

## Requirements
#### 1. Flask
#### 2. SQLAlchemy
#### 3. Blueprint
#### 4. PyOpenSSL
#### 5. Crypto Module Python

## Creating virtual environment for the applicatoion

```python -m venv venv```
<br><br>
```source venv/Scripts/activate``` 
<br><br>
## Installing Packages

```pip install flask pyOpenSSL cryptography```
<br><br>
```pip install requests install SQLAlchemy Flask-SQLAlchemy flask-blueprint```
<br><br>
```export FLASK_APP=blueprint```
<br><br>
```export FLASK_ENV=development```


## Initializing the database 

```C:/projects> python```
<br><br>
```> from blueprint import db```
<br><br>
```> from blueprint.extensions import db```
<br><br>
```> from blueprint import create_app```  
<br><br>
```> from blueprint.models import * ```
<br><br>
```> db.create_all(app=create_app())```
```> exit()```
<br><br>

## Starting Application

```flask run```
<br><br>


## Project Structure

```
root/
|- blueprint/
         |- certAuth/
                  |- __init__.py
                  |- auth.py
         |- models/
                  |- __init__.py
                  |- course.py
         |- routes/
                  |- __init__.py
                  |- api.py
         |- __init__.py
         |- custom_logger.py
         |- db.sqlite3
         |- extensions.py
         |- methods.py
|- venv/
|- README.md
```
<!---

### Json format of data in the database
```[
         {'name':'Python',
          'course_id':0,
          'description': 'interpret'
          },
           {'name':'java',
            'course_id': 1,
            'description': 'Bytecode'},
           {'name':'Cython',
            'course_id': 2,
            'description': 'Syn'},
           {'name':'C++',
            'course_id': 3,
            'description': 'Compiler'},
           ]```
<br><br><br>

-->




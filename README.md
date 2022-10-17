python -m venv venv 
source venv/Scripts/activate 
pip install flask pyOpenSSL cryptography
pip install requests install SQLAlchemy Flask-SQLAlchemy
export FLASK_APP=blueprint
export FLASK_ENV=development
flask run
touch blueprint/models.py
touch blueprint/extensions.py

[
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
           ]
## python

[from blueprint import db 
from blueprint.extensions import db 
from blueprint import create_app  
from blueprint.models import * 
db.create_all(app=create_app())]()
> exit()



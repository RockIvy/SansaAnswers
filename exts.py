# exts.py: 这个文件存在的意义就是解决循环引用问题

# flask-sqlchemy
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail

db = SQLAlchemy()
mail = Mail()

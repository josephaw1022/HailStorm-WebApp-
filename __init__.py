from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail # We need a mail port and server



# Connect with test database
db_path = os.path.join(os.path.dirname(__file__), 'site.db')
db_uri = 'sqlite:///{}'.format(db_path)

# Start the web app
app = Flask(__name__)

# Configure the app's url and encryption key
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'

# Configure the web app's database
db = SQLAlchemy(app)

#Encrypt the web app
bcrypt = Bcrypt(app)

# Login Manager function for managing pages the user can access
login_manager = LoginManager(app)
login_manager.login_view = 'login'
login_manager.login_message_category = 'info'

# Set up email
app.config['MAIL_SERVER']='smpt.googlemail.com'
app.config['MAIL_PORT']= 587
app.config['MAIL_USE_TLS']= True
app.config['MAIL_USERNAME']= os.environ.get('EMAIL_USER')
app.config['MAIL_USERNAME']= os.environ.get('EMAIL_PASS')
mail = Mail(app)

# Don't move this import. It's specifically after everthing for a reason.
from flaskblog import routes

#/var/www/flaskapp/flaskapp.wsgi
import sys
import os

sys.path.insert(0, '/var/www/flaskapp')

from flaskapp import app as application
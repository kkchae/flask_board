import os
#import secrets

BASE_DIR = os.path.dirname(__file__)

SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'pybo.db'))
SQLALCHEMY_TRACK_MODIFICATIONS = False

#SECRET_KEY = secrets.token_hex(nbytes=16)
SECRET_KEY = 'ff50a3496ac0083a258a7e1c6ea99b50'
from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','smtp.gmail.com', 'alog.post@gmail.com', '.golosa-afriki.ru']

#advised by manage.py check --deploy
# SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'


INSTALLED_APPS += ('lockdown', )
MIDDLEWARE += ('lockdown.middleware.LockdownMiddleware', )
LOCKDOWN_PASSWORDS = ('nyala', )
LOCKDOWN_FORM = 'lockdown.forms.LockdownForm'

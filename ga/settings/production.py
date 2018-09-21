from .base import *

DEBUG = True


ALLOWED_HOSTS = ['127.0.0.1','smtp.gmail.com', 'alog.post@gmail.com', 'www.golosa-afriki.ru', 'golosa-afriki.ru']

#advised by manage.py check --deploy
SECURE_CONTENT_TYPE_NOSNIFF = True
SECURE_SSL_REDIRECT = False
CSRF_COOKIE_SECURE = False
X_FRAME_OPTIONS = 'DENY'
#Uncomment it when not using lockdown!
#SESSION_COOKIE_SECURE = True


INSTALLED_APPS += ('lockdown', )
MIDDLEWARE += ('lockdown.middleware.LockdownMiddleware', )
LOCKDOWN_PASSWORDS = ('nyala', )
LOCKDOWN_FORM = 'lockdown.forms.LockdownForm'

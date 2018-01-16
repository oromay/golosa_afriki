from .base import *

DEBUG = False

ALLOWED_HOSTS = ['127.0.0.1','smtp.gmail.com', 'alog.post@gmail.com', '.golosa-afriki.ru']

INSTALLED_APPS += ('lockdown', )
MIDDLEWARE += ('lockdown.middleware.LockdownMiddleware', )
LOCKDOWN_PASSWORDS = ('nyala', )
LOCKDOWN_FORM = 'lockdown.forms.LockdownForm'

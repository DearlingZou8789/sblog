import os
import sys
path=os.path.dirname(__file__)
sys.path.append(path)
sys.path.append(os.path.dirname(path))
os.environ.setdefault('DJANGO_SETTINGS_MODULE','sblog.settings')
from django.core.wsgi import get_wsgi_application
application=get_wsgi_application()
#from django.core.wsgi import get_wsgi_application
#application=get_wsgi_application()

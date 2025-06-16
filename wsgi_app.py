# This file is used by Vercel to deploy the application

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'socialdots.settings')

# Get the WSGI application
application = get_wsgi_application()

# This is for Vercel deployment
app = application
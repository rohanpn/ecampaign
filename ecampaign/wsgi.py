"""
WSGI config for ecampaign project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os, sys, site, socket

VIRTUAL_ENV_PATH = '/home/rohan/pyenvs/ecampaign'
SITE_PACKAGES_DIR = os.path.join(VIRTUAL_ENV_PATH, 'lib/python2.7/site-packages')

site.addsitedir(SITE_PACKAGES_DIR)

activate_this = os.path.expanduser(os.path.join(VIRTUAL_ENV_PATH, "bin/activate_this.py"))
execfile(activate_this, dict(__file__=activate_this))

# Calculate the path based on the location of the WSGI script
project = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
if not project in sys.path:
    sys.path.insert(0, project)


os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ecampaign.settings")


from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

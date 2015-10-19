import os

APP_NAME = "sands"

PROJECT_ROOT = os.path.abspath(os.path.dirname(__file__))

STATIC_FOLDER = os.path.join(PROJECT_ROOT, "static")
TEMPLATE_FOLDER = os.path.join(PROJECT_ROOT, "templates")
SECRET_KEY = "EHTLJIOJ!@#$#JLkjdiks(0"

try:
    from sands.local_settings import *
except ImportError:
    print("Use original settings file instead of local_settings.py")
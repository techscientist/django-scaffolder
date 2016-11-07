import os

from django.apps import apps
from collections import OrderedDict as SortedDict


def reload_django_appcache():
    cache = apps

    cache.app_store = SortedDict()
    cache.app_models = SortedDict()
    cache.app_errors = {}
    cache.handled = {}
    cache.loaded = False

    for app in cache.get_app_configs():
        __import__(app.name)
        reload(app.module)


def clean_pyc_in_dir(dirpath):
    for root, _, files in os.walk(dirpath):
        for f in [f for f in files if os.path.splitext(f)[-1] == '.pyc']:
            os.remove(os.path.join(root, f))

import os

from celery import Celery
from django.conf import settings

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "sports_equipment_inventory.settings")

app = Celery("sports_equipment_inventory")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
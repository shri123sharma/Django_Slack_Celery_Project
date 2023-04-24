import os
from celery import Celery
from django.conf import settings
from celery.schedules import crontab
from datetime import timedelta
# from celery.schedules import crontab

# Set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'celery_send_mail_project.settings')

app = Celery('celery_send_mail_project',broker='redis://localhost:6379/')

# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django apps.
app.autodiscover_tasks(lambda : settings.INSTALLED_APPS)

@app.task(blind=True)
def debug_task(self):
    print('Request: {0!r}'.format(self.request))

app.conf.beat_schedule = {
    'SendEmail': {
        'task': 'celery_send_app_1.tasks.SendEmail',
        'schedule': crontab(minute='*/1'),
        
    },
}

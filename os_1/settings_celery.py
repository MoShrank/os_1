from celery.schedules import crontab
from datetime import date

DAYS = [1, 2, 3, 4, 5]

CELERY_BROKER_URL = 'amqp://'
CELERY_RESULT_BACKEND = 'djcelery.backends.database:DatabaseBackend'
CELERY_TIMEZONE = 'Europe/Berlin'
CELERY_IMPORTS = ('talk2x.tasks')

CELERYBEAT_SCHEDULE = {

    'match_user': {
        'task': 'talk2x.tasks.create_matches',
        'schedule' : crontab(hour=12, minute=0, day_of_week=DAYS),
        'args' : [date.today()]
    },

    'delete_future_lunches': {
        'task': 'talk2x.tasks.delete_future_lunch',
        'schedule' : crontab(hour=14, minute=0, day_of_week=DAYS)
    },

    'send_feedback': {
        'task' : 'talk2x.tasks.feedback',
        'schedule' : crontab(hour=15, minute=0, day_of_week=DAYS)
    },


}

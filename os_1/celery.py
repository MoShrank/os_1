from celery import Celery
import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'os_1.settings')

app = Celery('os_1')

app.config_from_object('django.conf:settings')
#app = Celery('tasks', backend='rpc://', broker='amqp://')
app.autodiscover_tasks(packages='', force=True)

#app.autodiscover_tasks(['os_1.talk2x'], force=True)



if __name__ == '__main__':
    app.start()

#   code taken from http://docs.celeryq.org/en/latest/index.html

from threading import Thread
import os
import sys
import subprocess

def main():
    django_thread = Thread(target=start_django, args=())
    django_thread.start()

    celery_thread = Thread(target=start_celery, args=())
    celery_thread.start()

def start_django():
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "os_1.settings")
    from django.core.management import execute_from_command_line

    django_args = []
    django_args.append(sys.argv[0])
    django_args.append('runserver')
    django_args.append('127.0.0.1:80')
    django_args.append('--noreload')
    execute_from_command_line(django_args)

def start_celery():
    subprocess.call(['celery', '-A', 'os_1', 'worker', '-l', 'info'])

if __name__ == "__main__":
    main()

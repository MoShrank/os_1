from celery import shared_task

from .send_email import send_email

from .matching import match_user
from .models import Lunch
from datetime import date

#@shared.task()
def send_emails(lunch):

    receiver = lunch.user.all()

    send_email('lunch', receiver[0].email, { 'partner' : receiver[1], 'restaurant' : lunch.restaurant })

    send_email('lunch', receiver[1].email, { 'partner' : receiver[0], 'restaurant' : lunch.restaurant })


@shared_task()
def create_matches():

    match_user()

    lunches = Lunch.objects.filter(date=date.today())

    for l in lunches:
        send_emails(l)  #.delay(l)

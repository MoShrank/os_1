from celery import shared_task
from .matching import match_user
from .models import Lunch, FutureLunch
from datetime import date
from django.core.mail import send_mail
from .get_message import get_message
from django.conf import settings


@shared_task(name='send_email')
def send_email(subject, to, context):

    send_mail(subject, get_message(subject, context), settings.EMAIL_HOST_USER, [to])


@shared_task(name='create_matches')
def create_matches():

    match_user()

    lunches = Lunch.objects.filter(date=date.today())

    for l in lunches:

        receiver = l.user.all()

        send_email.delay('lunch', receiver[0].email, { 'partner' : receiver[1], 'restaurant' : l.restaurant })

        send_email.delay('lunch', receiver[1].email, { 'partner' : receiver[0], 'restaurant' : l.restaurant })


@shared_task(name='delete_future_lunch')
def delete_future_lunch():

    FutureLunch.objects.filter(date=date.today()).delete()

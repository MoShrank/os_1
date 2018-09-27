from celery import shared_task
from .matching import match_user
from .models import Lunch, FutureLunch
from datetime import date
from django.core.mail import send_mail
from .get_message import get_message
from django.conf import settings


@shared_task()
def send_email_task(subject, to, context):

    send_mail(subject, get_message(subject, context), settings.EMAIL_HOST_USER, [to])


@shared_task()
def create_matches(date):

    match_user()

    lunches = Lunch.objects.filter(date=date)

    for l in lunches:

        receiver = l.user.all()

        send_email.delay('lunch', receiver[0].email, { 'partner' : receiver[1], 'restaurant' : l.restaurant })

        send_email.delay('lunch', receiver[1].email, { 'partner' : receiver[0], 'restaurant' : l.restaurant })


@shared_task()
def delete_future_lunch():

    FutureLunch.objects.filter(date=date.today()).delete()


@shared_task()
def feedback():

    lunches = Lunch.objects.filter(date=date.today)

    for l in lunches:

        receiver = l.user.all()

        send_email.delay('lunch feedback', receiver[0].email, { 'user' : receiver[0], 'link' : 'talk2x.com' })

        send_email.delay('lunch feedback', receiver[1].email, { 'user' : receiver[1], 'link' : 'talk2x.com' })

from celery import shared_task

#from .send_email import sendemail

from .matching import match_user
from .models import Lunch
from datetime import date

#@shared.task()
def send_email(lunch):

    receiver = lunch.user.all()

 #   sendemail(receiver[0].email, date.today().strftime("%A"), lunch.restaurant.name, receiver[1].first_name)

 #   sendemail(receiver[1].email, date.today().strftime("%A"), lunch.restaurant.name, receiver[0].first_name )


@shared_task()
def create_matches():
    return 0
'''
    match_user()

    lunches = Lunch.objects.filter(date=date.today())

    for l in lunches:
        send_email(l)  #.delay(l)
'''

    #return 0

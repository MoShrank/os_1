from celery import shared_task
from .send_email import sendemail
from .matching import match_user
#from matching import create_lunch_entry



@shared_task()
def match_user():

    #match user3

    #send out email

    return 0

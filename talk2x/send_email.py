from django.core.mail import send_mail
from django.conf import settings


subject = 'Lunch'



def get_message_user(day, partner1, restaurant,  partner2 = ''):
    ret_str = 'You are going to have Lunch at 1pm on ' + day + ' with '
    if not partner2 == '':
          ret_str = ret_str + partner2 + ' and '

    ret_str = ret_str + partner1 + ' at ' + restaurant

    return ret_str

def get_message_restaurant():
    return 0

def sendemail(receiver, day, restaurant, partner):
    send_mail(subject, get_message_user(day, partner, restaurant), settings.EMAIL_HOST_USER, [receiver])


def send_activation_email(receiver, message):
    send_mail('activate your account', message, settings.EMAIL_HOST_USER, [receiver])

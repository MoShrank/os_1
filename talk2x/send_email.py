from django.core.mail import send_mail
from django.conf import settings


email = 'moritz.e50@gmail.com'
day = 'monday'
name = 'welf'
restaurant = 'factory'


subject = 'Lunch'

recipient_list = [ email ]


def get_message_user(day, partner1, restaurant,  partner2 = ''):
    ret_str = 'You are going to have Lunch at 1pm on ' + day + ' with '
    if not partner2 == '':
          ret_str = ret_str + partner2 + ' and '

    ret_str = ret_str + partner1 + ' at ' + restaurant

    return ret_str

def get_message_restaurant():
    return 0

def sendemail():
    send_mail(subject, '', settings.EMAIL_HOST_USER, recipient_list)

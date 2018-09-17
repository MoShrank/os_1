from django.core.mail import send_mail
from django.conf import settings

from django.template.loader import get_template



def lunch():

    context = {
        'name' : 'hi'
    }

    email = get_template('emails/lunch_one_person.txt')

    return email.render(context)

def lunch_feedback():
    return 0

def lunch_confirmation():
    return 0

def confirm_registration():
    return 0

def get_message(subject):

    switch_messages = { 'confirm registration' : confirm_registration,
                        'lunch confirmation' : lunch_confirmation,
                        'lunch feedback:' : lunch_feedback,
                        'lunch' : lunch
                        }


    function = switch_messages.get(subject, lambda: 'invalid email')

    return function()


def send_email(subject, message, to):

    send_mail(subject, get_message(), settings.EMAIL_HOST_USER, [to])

#def sendemail(receiver, day, restaurant, partner):
#send_mail(subject, get_message_user(day, partner, restaurant), settings.EMAIL_HOST_USER, [receiver])

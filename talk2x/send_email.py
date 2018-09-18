from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import get_template



def lunch(context):

    if 'partner2' in context:

        email = get_template('emails/lunch_one_person.txt')

    else:

        email = get_template('emails/lunch_two_persons.txt')

    return email.render(context)

def lunch_feedback(context):

    email = get_template('emails/lunch_feedback.txt')

    return email.render(context)

def confirm_registration(context):

    email = get_template('emails/confirm_registration.txt')

    return email.render(context)

#returns email as string related to subject --> right context must be given
def get_message(subject, context):

    switch_messages = { 'confirm registration' : confirm_registration,
                        'lunch feedback:' : lunch_feedback,
                        'lunch' : lunch
                        }


    function = switch_messages.get(subject, 'invalid email')

    return function(context)


def send_email(subject, to, context):

    send_mail(subject, get_message(subject, context), settings.EMAIL_HOST_USER, [to])

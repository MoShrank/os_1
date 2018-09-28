from django.template.loader import get_template



def lunch(context):

    email = get_template('emails/lunch_one_person.txt')

    return email.render(context)

def lunch_feedback(context):

    email = get_template('emails/lunch_feedback.txt')

    return email.render(context)

def confirm_registration(context):

    email = get_template('emails/confirm_registration.txt')

    return email.render(context)

def confirmation_lunch(context):

    email = get_template('emails/confirmation_lunch.txt')

    return email.render(context)

#returns email as string related to subject --> right context must be given
def get_message(subject, context):

    switch_messages = { 'confirm registration' : confirm_registration,
                        'lunch feedback' : lunch_feedback,
                        'lunch' : lunch,
                        'confirm lunch' : confirmation_lunch,
                        }


    function = switch_messages.get(subject, 'invalid email')

    return function(context)

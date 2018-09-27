from django.core.exceptions import ValidationError
from datetime import *

def validate_code_mail(email):
    code = 'code.berlin'
    try:
        index = email.index('@') + 1
    except:
        return False
    email = email[index:]

    if code != email:
        raise ValidationError('no valid email')



def validate_lunch_date(date):
    if date < date.today():
        raise ValidationError('date is in the past')
    elif (date - date.today()).days > 14:
        raise ValidationError('too far in the future')
    #elif date == date.today() and (datetime.now().time().hour) > 12:
    #    raise ValidationError('too late')

from django.core.exceptions import ValidationError
from datetime import *

def validate_code_mail(email):
    code = 'code.berlin'
    try:
        index = email.index('@') + 1
    except:
        return False
    email = email[index:]

#    if code != email:
#        raise ValidationError('please use your code email address to signup')



def validate_lunch_date(date_):
    if date_ < date.today():
        raise ValidationError('date is in the past')
    elif (date_ - date.today()).days > 14:
        raise ValidationError('too far in the future')
    elif date_ == date.today() and (datetime.now().time().hour) > 12:
        raise ValidationError('too late')
    elif date_.weekday() == 5 or date_.weekday() == 6:
        raise ValidationError('unfortunately you cannot have lunch during the weekend')

from django.core.exceptions import ValidationError


def validate_code_mail(email):
    code = 'code.berlin'
    try:
        index = email.index('@') + 1
    except:
        return False
    email = email[index:]

    if code != email:
        raise ValidationError('no valid email')

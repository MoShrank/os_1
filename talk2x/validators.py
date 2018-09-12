from django.core.exceptions import ValidationError


def validate_code_mail(email):
    code = 'code.berlin'
    try:
        index = email.index('@') + 1
    except:
        return False
    email = email[index:]

    for n in range(11):
        if code[n] != email[n]:
            raise ValidationError('no valid email')

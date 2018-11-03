from .tasks import send_email_task
from .models import FutureLunch, User
from django.db.models import Q

def send_reminder_email():

    lunches = FutureLunch.objects.all()

    for l in lunches:
        email = l.user.email
        date = l.date
        send_email_task.delay('reminder', email, {'date' : date})

def send_reminder_change_email():

    user = User.objects.all().exclude(email__endswith='@code.berlin')

    for u in user:
        email = u.email
        print(email)
        send_email_task.delay('reminder', email, {'user' : user})

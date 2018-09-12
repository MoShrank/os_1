from django.core.mail import send_mail
from django.conf import settings


email = 'moritz.e50@gmail.com'
day = 'monday'
name = 'welf'
restaurant = 'factory'


subject = 'Lunch'
message = 'You are going to have Lunch at 1pm on ' + day + ' with ' + name + ' at ' + restaurant
email_from = settings.EMAIL_HOST_USER
recipient_list = [ email ]




def sendemail():
    send_mail(subject, message, email_from, recipient_list)

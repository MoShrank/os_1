from django.test import TestCase
from .models import *
from .send_email import *
from .tasks import *

# Create your tests here.


def test_email():

    partner = User.objects.get(first_name='Moritz')
    restaurant = Restaurant.objects.get(name='pizza')

    context = {
        'partner' : partner,
        'restaurant' : restaurant
    }

    return get_message('lunch', context)

def test_():

    for n in range(250):

        re = send_email_test.delay()

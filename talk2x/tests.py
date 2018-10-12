from django.test import TestCase
from .models import *
#from .send_email import *
from .tasks import *

# Create your tests here.


def send_test_email():

    #partner = User.objects.get(first_name='Moritz')
    #restaurant = Restaurant.objects.get(name='pizza')

    context = {
        '1' : 'partner',
        '2' : 'restaurant'
    }

    send_email_task('confirm lunch', 'moritz.eich@code.berlin', context)

def test_():

    for n in range(250):

        re = send_email_test.delay()

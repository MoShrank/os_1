import random
from datetime import date
from .models import FutureLunch


def match_user(user_list, length):

    # first: check if even or odd number

    lunches = FutureLunch.objects.filter(date=date.today())
    x = 0
    for l in lunches:
        print(x)
        x = x +1


'''
    if((length % 2) > 0):
        rnd = random.randint(0, length)
        length = length - 1
        user1 = user_list[rnd]
        user_list.pop(rnd)

    for n in (length/2)
        rnd = random.randint(0, length)
        length = length - 1
        user2 = user_list[rnd]
        user_list.pop(rnd)
        rnd = random.randint(0, length)
        lenght = length - 1
        user3 = user_list[rnd]
        user_list.pop(rnd)

        lunch = Lunch(name='test', date=datetime.date())
        lunch.save()
'''


    #return 0


def match_restaurant_to_user(user_list, restaurant_list):
    return 0

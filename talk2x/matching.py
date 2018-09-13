import random
from datetime import date
from .models import FutureLunch, Restaurant, Lunch, User


def match_user():

    #get all needed values

    user_list = []

    lunches = FutureLunch.objects.filter(date=date.today())

    for l in lunches:
        user_list.append(l.user)

    length = len(user_list)
    random.shuffle(user_list)

    restaurants = Restaurant.objects.all()
    restaurant_list = restaurants.values()

    # first: check if even or odd number

    if (length % 2) > 0:

        length = length - 1

    length = int(length / 2)

    #match user

    for index in range(length):

        lunch = Lunch(date=date.today())
        lunch.save()

        lunch.user.add(user_list[0])
        user_list.pop(0)
        lunch.user.add(user_list[0])
        user_list.pop(0)

        #get renadom resaurant and add it to Lunch

        #rnd = random.randint(0, len(restaurant_list))
        lunch.restaurant = Restaurant.objects.get(id=restaurant_list[index]['id'])
        lunch.save()

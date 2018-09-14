import random
from datetime import date
from .models import FutureLunch, Restaurant, Lunch, User


def match_user():

    # first: check if even or odd number

    user_list = []

    lunches = FutureLunch.objects.filter(date=date.today())
    restaurants = Restaurant.objects.all()
    restaurant_list = restaurants.values()

    for l in lunches:
        user_list.append(l.user.email)

    length = len(user_list)
    random.shuffle(user_list)

    if (length % 2) > 0:

        length = length - 1

    length = int(length / 2)

    for index in range(length):

        lunch = Lunch(date=date.today())
        lunch.save()

        lunch.user.add(User.objects.get(email=user_list[0]))
        user_list.pop(0)
        lunch.user.add(User.objects.get(email=user_list[0]))
        user_list.pop(0)

        lunch.restaurant = Restaurant.objects.get(id=restaurant_list[index]['id'])
        lunch.save()

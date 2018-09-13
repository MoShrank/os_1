import random
from datetime import date
from .models import FutureLunch, Restaurant, Lunch, User


def match_user(user_list, length):

    # first: check if even or odd number

    random.shuffle(user_list)

    lunches = FutureLunch.objects.filter(date=date.today())
    restaurants = Restaurant.objects.all()
    restaurant_list = restaurants.values()
    random.shuffle(restaurant_list)

    if (length % 2) > 0:

        length = length - 1

    length = int(length / 2)

    for index in range(length):

        lunch = Lunch(name='test', date=date.today())
        lunch.save()

        lunch.user.add(User.objects.get(email=user_list[0]))
        user_list.pop(0)
        lunch.user.add(User.objects.get(email=user_list[0]))
        user_list.pop(0)

        #get renadom resaurant and add it to Lunch

        #rnd = random.randint(0, len(restaurant_list))
        #lunch.restaurant = Restaurant.objects.get(id=restaurant_list[rnd]['id'])
        lunch.save()

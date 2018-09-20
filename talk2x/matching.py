import random
from datetime import date
from .models import FutureLunch, Restaurant, Lunch, User


#turns restaurant queryset into list of ids and shuffles it
def get_random_restaurant_list(queryset):

    restaurant_list = []

    for r in queryset:
        restaurant_list.append(r.id)

    random.shuffle(restaurant_list)
    return restaurant_list

#turns user queryset into list of email and shuffles it
def get_random_user_list(queryset):

    user_list = []

    for u in queryset:
        user_list.append(u.user.email)

    random.shuffle(user_list)
    return user_list

#matches two (or three) users and a restaurant and creates Lunch entry in database
def match_user():

    #get all values
    third_user = ''

    restaurant_list = get_random_restaurant_list(Restaurant.objects.all())

    #only gets FutureLunches from today and where is_active is true
    user_list = get_random_user_list(FutureLunch.objects.filter(date=date.today()).filter(is_active=True))

    restaurant_length = len(restaurant_list)
    user_length = len(user_list)

    # first: check if even or odd number
    if (user_length % 2) > 0:

        third_user = user_list[0]
        user_list.pop(0)

        user_length = user_length - 1

    user_length = int(user_length / 2)

    #match user and restaurants and create lunch entry
    for index in range(user_length):

        lunch = Lunch(date=date.today())
        lunch.save()

        lunch.user.add(User.objects.get(email=user_list[0]))
        user_list.pop(0)
        lunch.user.add(User.objects.get(email=user_list[0]))
        user_list.pop(0)


        if restaurant_length == 0:
            restaurant_list = get_random_restaurant_list(Restaurant.objects.all())
            restaurant_length = len(restaurant_list)

        else:
            lunch.restaurant = Restaurant.objects.get(id=restaurant_list[index])
            restaurant_list.pop(index)
            restaurant_length = restaurant_length - 1
            lunch.save()

    if not third_user == '':
        lunch.user.add(User.objects.get(email=third_user))

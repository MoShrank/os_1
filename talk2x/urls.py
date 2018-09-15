from django.urls import path, include
from . import views
from .views import Signup, Profile, EditProfile, CreateFutureLunch
from django.contrib.auth import views as auth_views
#from .views import newRestaurant


urlpatterns = [
    path('', views.home, name='home'),

    path('login/', auth_views.login, name='login'),
    path('logout/', auth_views.logout, name='logout'),
    path('signup/', Signup.as_view()),
    path('activate/<int:pk>/<str:token>',
        views.activate, name='activate'),
    #path('reset-password')

    path('profile/<slug:slug>-<int:user_id>', Profile.as_view()),
    path('profile/<slug:slug>-<int:user_id>/edit', EditProfile.as_view()),
    path('lunch/', CreateFutureLunch.as_view()),
    path('lunch/<int:lunch_id>/cancel', views.cancel_lunch, name='cancel_lunch'),
    path('contact/', views.contact, name='contact'),


    path('', include('social_django.urls', namespace='social'))
]

from django.urls import path, include
from . import views
from .views import  Signup, Profile, EditProfile, CreateFutureLunch
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),

    path('login/', auth_views.LoginView.as_view(redirect_authenticated_user=True)),
    path('logout/', auth_views.LogoutView.as_view()),
    path('signup/', Signup.as_view()),
    path('activate/', views.activate_page, name='activate_page'),
    path('activate/<int:pk>/<str:token>/', views.activate, name='activate'),
    path('activate_email', views.activation_email, name='activation_email'),


    path('password_reset', auth_views.PasswordResetView.as_view(template_name='registration/password_reset.html'), name='password_reset'),
    path('password_reset/confirm', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm')

    path('accounts/', include('django.contrib.auth.urls')),

    path('profile/<slug:slug>-<int:user_id>/', Profile.as_view(), name='profile'),
    path('profile/<slug:slug>-<int:user_id>/edit/', EditProfile.as_view(), name='profile_edit'),
    path('profile/<slug:slug>-<int:user_id>/subscribe/', views.subscribe, name='subscribe'),
    path('profile/<slug:slug>-<int:user_id>/unsubscribe/', views.unsubscribe, name='unsubscribe'),
    path('lunch/', CreateFutureLunch.as_view(), name='lunch'),
    path('lunch/<int:lunch_id>/cancel/', views.cancel_lunch, name='cancel_lunch'),
    path('contact/', views.contact, name='contact'),


    #path('social/', include('social_django.urls', namespace='social'))
]

if settings.DEBUG is True:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

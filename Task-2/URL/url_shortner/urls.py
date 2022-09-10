from django.urls import path
from .views import *
from knox import views as knox_views


urlpatterns = [
    path('', ShortenerListAPIView.as_view(), name='all'),
    path('create/', ShortenerCreateApiView.as_view(), name='create'),
    path('register/', RegisterAPI.as_view(), name='register'),
    path('login/', LoginAPI.as_view(), name='login'),
    path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('profile/', Profile.as_view(), name='profile'),
    path('change_password/', ChangePasswordView.as_view(), name='change_password'),
    path('<str:shortener_link>/', Redirector.as_view(), name='redirector'),

]

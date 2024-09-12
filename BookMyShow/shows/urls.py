from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views

urlpatterns = [
    path('', views.index),
    path('movies',views.movies),
    path('movies/detail/<int:id>',views.movie_detail,name='movies/detail'),
    path('theatre/list/<int:id>',views.theatre_select,name='theatre/list'),
    path('seat/selection/<int:showtiming_id>', views.seat_layout,name='seat/selection'),
    path('signup',views.signup,name='signup'),
    path('login',views.user_login,name='login'),
    path('logout',views.user_logout,name='logout')
]
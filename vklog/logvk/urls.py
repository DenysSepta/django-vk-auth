from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.friends_out, name='friends_out'),

]

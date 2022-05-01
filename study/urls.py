from django.urls import path
from . import views

#spotify linking
#app_name = 'study'

urlpatterns = [
    path('', views.home, name='home'),
    path('about', views.about, name='about')
]

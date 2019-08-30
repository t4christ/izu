from django.urls import path
from django.contrib import admin

from .views import (
	home,
    about,
    contact
	)

app_name="building"

urlpatterns = [
	path('',home,name='home'),
    path('about',about,name='about'),
    path('contact',contact,name='contact'),

]

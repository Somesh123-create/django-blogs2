from  django.urls import path
from .views import index, meetup_detail, register_success

app_name = 'meetup'

urlpatterns = [
    path('', index, name='home'),
    path('<slug:slug>/register_success', register_success, name='register_success'),
    path('<slug:slug>', meetup_detail, name='meet_detail'),

]

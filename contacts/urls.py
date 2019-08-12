from django.urls import path
from .views import contact, contact_list, contact_detail, contact_search

app_name = 'contact'

urlpatterns = [

    path('contact', contact, name='contact'),
    path('contact/messages/', contact_list, name='contacts-list'),
    path('messages/<int:contact_id>/', contact_detail, name='contact-details'),
    path('contact/message/search/', contact_search, name='contact-search')
]
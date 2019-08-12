from django.urls import path
from . import views
from bookings.models import Booking



app_name='pages'

urlpatterns = [
    path('', views.index, name='index'),
    path('job/<int:booking_id>/', views.job, name='job'),
    path('job/search/', views.job_search, name ='job-search')

]

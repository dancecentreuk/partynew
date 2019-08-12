from django.urls import path
from .views import venues, venue_detail, VenueUpdateView,VenueCreateView, venue_search


app_name='cities'

urlpatterns = [

    path('', venues, name='venues'),
    path('venue/<int:venue_id>/', venue_detail, name='venue-detail'),
    path('venue/<int:pk>/update', VenueUpdateView.as_view(), name='venue-update'),
    path('new/', VenueCreateView.as_view(), name='venue-create' ),
    path('search/', venue_search, name='venue-search')


]
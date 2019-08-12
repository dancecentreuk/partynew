from django.shortcuts import render, get_object_or_404
from .models import Venue
from django.views.generic import UpdateView, CreateView
from .choices import city_choices
from django.contrib.auth.decorators import login_required
from django.core.exceptions import PermissionDenied
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin


# Create your views here.

def authorised_only(function):

    def _inner(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner

@login_required
@authorised_only
def venues(request):
    venues = Venue.objects.all()

    context = {
        'venues': venues,
        'city_choices': city_choices
    }

    return render(request, 'cities/venues.html', context)


@login_required
@authorised_only
def venue_detail(request, venue_id):

    venue = get_object_or_404(Venue, pk=venue_id)

    context = {

        'venue': venue

    }
    return render(request, 'cities/venue-detail.html', context)


class VenueCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Venue
    template_name = 'cities/venue_form.html'
    fields = '__all__'

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class VenueUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Venue
    template_name = 'cities/venue_form.html'
    fields = '__all__'

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


@login_required
@authorised_only
def venue_search(request):

    queryset_list = Venue.objects.all()

    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__name__icontains=city)


    context ={
        'venues': queryset_list,
        'city_choices': city_choices
    }
    return render(request, 'cities/venue_search.html', context)
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Contact
from cities.choices import city_choices
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required



def authorised_only(function):

    def _inner(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner



def contact(request):
    if request.method == 'POST':
        booking_id = request.POST['booking_id']
        booking = request.POST['booking_name']
        name = request.POST['name']
        email = request.POST['email']
        mobile = request.POST['mobile']
        message = request.POST['message']
        experience = request.POST['experience']
        dance_school = request.POST['dance_school']
        user_id = request.POST['user_id']
        contact_city = request.POST['contact_city']
        booking_city = request.POST['booking_city']

        contact = Contact(booking=booking, booking_id=booking_id, booking_city=booking_city, name=name,
                          email=email, mobile=mobile, message=message, experience=experience,
                          dance_school=dance_school, user_id=user_id, contact_city=contact_city)

        contact.save()

        messages.success(request, 'Your request has been submitted')

        return redirect('/job/'+booking_id)


@login_required
@authorised_only
def contact_list(request):

    contact_list = Contact.objects.all().order_by('-contact_date')


    context={

        'teacher_messages': contact_list,
        'city_choices': city_choices


    }
    return render(request, 'contacts/inbox.html', context)


def contact_detail(request, contact_id):
    teacher_message = get_object_or_404(Contact, pk=contact_id)

    context = {
        'teacher_message': teacher_message
    }

    return render(request, 'contacts/contact_detail.html', context)


@login_required
@authorised_only
def contact_search(request):
    queryset_list = Contact.objects.all().order_by('-contact_date')

    if 'name' in request.GET:
        name = request.GET['name']
        if name:
            queryset_list = queryset_list.filter(name__icontains=name)


    if 'teacher_city' in request.GET:
        teacher_city = request.GET['teacher_city']
        if teacher_city:
            queryset_list = queryset_list.filter(contact_city__icontains=teacher_city)

    if 'booking_city' in request.GET:
        booking_city = request.GET['booking_city']
        if booking_city:
            queryset_list = queryset_list.filter(booking_city__icontains=booking_city)


    context={

        'teacher_messages': queryset_list,
        'city_choices': city_choices
    }




    return render(request, 'contacts/contacts_search.html', context)




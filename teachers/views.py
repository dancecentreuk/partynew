from django.shortcuts import render, get_object_or_404
from .models import Teacher
from cities.choices import city_choices, dance_styles
from django.views.generic import UpdateView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.exceptions import PermissionDenied
from django.contrib.auth.decorators import login_required




def authorised_only(function):

    def _inner(request, *args, **kwargs):
        if not request.user.is_staff:
            raise PermissionDenied
        return function(request, *args, **kwargs)
    return _inner


@login_required
@authorised_only
def teacher_list(request):
    teachers = Teacher.objects.all()

    context = {
        'teachers':teachers,
        'city_choices':city_choices,
        'dance_styles': dance_styles
    }

    return render(request, 'teachers/teachers.html', context)


@login_required
@authorised_only
def teacher_detail(request, teacher_id):

    teacher = get_object_or_404(Teacher, pk=teacher_id)

    context = {
        'teacher': teacher
    }
    return render(request, 'teachers/teachers-detail.html', context)



class TeacherUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Teacher
    template_name = 'teachers/teachers_form.html'
    fields = '__all__'

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False


class TeacherCreateView(LoginRequiredMixin, UserPassesTestMixin, CreateView):
    model = Teacher
    template_name = 'teachers/teachers_form.html'
    fields = '__all__'

    def test_func(self):
        if self.request.user.is_staff:
            return True
        return False



@login_required
@authorised_only
def teachers_search(request):

    queryset_list = Teacher.objects.all()



    if 'teachers_name' in request.GET:
        teachers_name = request.GET['teachers_name']
        if teachers_name:
            queryset_list = queryset_list.filter(first_name__icontains=teachers_name)

    # City
    if 'city' in request.GET:
        city = request.GET['city']
        if city:
            queryset_list = queryset_list.filter(city__icontains=city)

    # Dance style
    if 'style' in request.GET:
        style = request.GET['style']
        if style:
            queryset_list = queryset_list.filter(speciality__icontains=style)


    context = {

        'teachers': queryset_list,
        'city_choices': city_choices,
        'dance_styles': dance_styles



    }
    return render(request, 'teachers/teachers_search.html', context)







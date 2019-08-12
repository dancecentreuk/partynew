from django.urls import path
from .views import teacher_list, teachers_search, teacher_detail, TeacherUpdateView, TeacherCreateView


app_name = 'teachers'

urlpatterns = [
    path('', teacher_list, name='teachers'),
    path('teacher/<int:teacher_id>/', teacher_detail, name='teacher-detail'),
    path('teacher/<int:pk>/update/', TeacherUpdateView.as_view(), name='teacher-update' ),
    path('new', TeacherCreateView.as_view(), name='teacher-create'),
    path('search', teachers_search, name='teachers-search' )
]
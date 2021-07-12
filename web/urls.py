from django.urls import path
from web.views import about, contact, detail, index, studentRegis, subjectRegis

urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:id>', detail, name='detail'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('regis/student/', studentRegis, name='regis-student'),
    path('regis/subject/', subjectRegis, name='regis-subject'),
]

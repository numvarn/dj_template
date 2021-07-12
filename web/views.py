from web.models import StudentForm, Subject, SubjectForm
from django.shortcuts import render

# Create your views here.


def index(request):
    context = {}
    context['subjects'] = Subject.objects.all()
    return render(request, "index.html", context)


def detail(request, id):
    context = {}
    subjects = Subject.objects.filter(id=id)
    for subject in subjects:
        context['subject'] = subject

    return render(request, "detail.html", context)


def about(request):
    return render(request, "about.html")


def contact(request):
    return render(request, "contact.html")


def studentRegis(request):
    context = {}
    if request.method == "POST":
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error")

    context['form'] = StudentForm()
    return render(request, "regis_student.html", context)


def subjectRegis(request):
    context = {}
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            print("Error")

    context['form'] = SubjectForm()
    return render(request, 'regis_subject.html', context)

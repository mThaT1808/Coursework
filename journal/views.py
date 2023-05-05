from django.shortcuts import render
from django.http import HttpRequest, HttpResponseRedirect

from journal.models import Teacher, Group, Lesson, Student, Mark, Subject
from journal import forms


# Create your views here.

def main(request):
    teachers = Teacher.objects.all()
    groups = Group.objects.all()
    context = {
        'teachers': teachers,
        'groups': groups,
    }
    return render(request, 'main_page.html', context)

def teachers(request):
    teachers = Teacher.objects.all()
    return render(request, 'teachers.html', {'teachers': teachers})

def groups(request):
    groups = Group.objects.all()
    return render(request, 'groups.html', {'groups': groups})

def timetable_by_group(request, id: int):
    group = Group.objects.get(pk=id)
    lessons = Lesson.objects.filter(group=id)
    students = Student.objects.filter(group=id)
    marks = Mark.objects.all()

    context = {
        'group': group,
        'lessons': lessons,
        'students': students,
        'marks': marks,
    }
    return render(request, 'group_list.html', context)

def subjects_list(request):
    subjects = Subject.objects.all()


    context = {
        'subjects': subjects,
    }
    return render(request, 'subjects_list.html', context)

def journal(request, id: int):
    if request.method == 'POST':
        form = forms.Group_form(request.POST)
        if form.is_valid():
            obj = Group()
            obj.name = form.cleaned_data['group_id']

            return HttpResponseRedirect(f'/groups/subjects/{id}/')
    else:
        form = forms.Group_form()
    context = {

    }
    return render(request, 'journal.html', context)

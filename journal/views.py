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

def journal(request, id: int, id1: int):
    group = Group.objects.get(pk=id1)
    subject = Subject.objects.get(pk=id)
    students = Student.objects.filter(group=id1)
    lessons = Lesson.objects.filter(group=id1, subject=id)
    marks = Mark.objects.all()
    context = {
        'group': group,
        'subject': subject,
        'students': students,
        'lessons': lessons,
        'marks': marks,
    }
    return render(request, 'journal.html', context)

def prejournal(request, id: int):
    groups = Group.objects.all()
    context = {
        'groups': groups,
        'id': id,
    }
    return render(request, 'prejournal.html', context)

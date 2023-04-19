from django.shortcuts import render

from journal.models import Teacher, Group


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
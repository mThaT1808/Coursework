from django.db import models
import datetime

# Create your models here.

class Mark(models.Model):
    CHOICES = (
        ("H", "H"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        (".", "."),
    )
    name = models.CharField(
        max_length=1,
        choices=CHOICES,
        null=False,
        blank=False
    )
    student = models.ForeignKey(
        'Student',
        on_delete=models.CASCADE
    )
    lesson = models.ForeignKey(
        'Lesson',
        on_delete=models.CASCADE,
        null=False,
        blank=False
    )

class Lesson(models.Model):
    name = models.CharField(max_length=20)
    teacher = models.ForeignKey('Teacher', on_delete=models.PROTECT, null=True, blank=True)
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT, null=True, blank=True)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=True, blank=True)
    date = models.DateField(help_text='__.__.____', default=datetime.date.today, null=False, blank=False)


class Teacher(models.Model):
    name = models.CharField(max_length=20)


class Student(models.Model):
    name = models.CharField(max_length=20)
    group = models.ForeignKey('Group', on_delete=models.PROTECT, null=False, blank=False)

class Group(models.Model):
    YEAR_CHOICES = (
        ("1", "1"),
        ("2", "2"),
        ("3", "3"),
        ("4", "4"),
        ("5", "5"),
        ("6", "6"),
        ("7", "7"),
        ("8", "8"),
        ("9", "9"),
        ("-", "-"),
    )
    LETTER_CHOICES = (
        ("А", "А"),
        ("Б", "Б"),
        ("В", "В"),
        ("Г", "Г"),
        ("Д", "Д"),
        ("-", "-"),
    )
    letter = models.CharField(max_length=1, choices=LETTER_CHOICES, default='-')
    study_year = models.CharField(max_length=2, choices=YEAR_CHOICES, default='-')
class Subject(models.Model):
    name = models.CharField(max_length=20)

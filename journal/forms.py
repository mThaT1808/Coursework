from django import forms
from journal import models

class Group_form(forms.Form):
    group_id = forms.ChoiceField(label='Выберите группу:')

from django import forms
from django.forms import widgets


CHOICES = [('new', 'Новая'), ('in_progress', 'В процессе'), ('done', 'Сделано')]
class ToDoListForm(forms.Form):
    description = forms.CharField(max_length=3000, required=True, label='Описание', widget=widgets.Textarea)
    status = forms.ChoiceField(required=True, label='Статус', choices=CHOICES)
    date = forms.CharField(max_length=100, required=False, label='Дата')
    detailed_desc = forms.CharField(max_length=2000, required=False, label='Детальное описание', widget=widgets.Textarea)
from django.db import models

# Create your models here.

class ToDoList (models.Model):
    description = models.TextField(max_length=3000, null=False, blank=False, verbose_name='Описание')
    status = models.TextField(max_length=20, null=False, blank=False, default='New', verbose_name='Статус')
    date = models.DateField(null=True, verbose_name='Дата')
    detailed_desc = models.TextField(max_length=2000, default='', verbose_name='Подробное описание')

    def __str__(self):
        return f'{self.pk}. {self.description}. {self.status}. {self.date}'
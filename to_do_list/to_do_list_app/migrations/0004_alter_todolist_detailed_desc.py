# Generated by Django 4.2.7 on 2023-12-07 13:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('to_do_list_app', '0003_todolist_detailed_desc_alter_todolist_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todolist',
            name='detailed_desc',
            field=models.TextField(blank=True, default='', max_length=2000, null=True, verbose_name='Подробное описание'),
        ),
    ]

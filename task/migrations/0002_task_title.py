# Generated by Django 5.0.6 on 2024-06-18 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='title',
            field=models.CharField(default='', max_length=100),
        ),
    ]

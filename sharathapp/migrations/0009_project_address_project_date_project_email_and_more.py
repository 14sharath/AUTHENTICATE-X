# Generated by Django 4.1.7 on 2023-11-14 19:15

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sharathapp', '0008_remove_project_date_remove_project_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='address',
            field=models.TextField(default='', max_length=1000),
        ),
        migrations.AddField(
            model_name='project',
            name='date',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='project',
            name='email',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='firstname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AddField(
            model_name='project',
            name='secondname',
            field=models.CharField(default='', max_length=100),
        ),
        migrations.AlterField(
            model_name='project',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.DeleteModel(
            name='CustomUser',
        ),
    ]

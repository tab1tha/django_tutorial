# Generated by Django 4.2.5 on 2023-09-12 08:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sfdata', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='date_uploaded',
        ),
        migrations.RemoveField(
            model_name='file',
            name='file_name',
        ),
        migrations.AddField(
            model_name='file',
            name='file_path',
            field=models.CharField(default='C:\\Users\\tambe.tabitha\\django_tutorial\\mysite\\sfdata\\admin.py', max_length=255),
            preserve_default=False,
        ),
    ]

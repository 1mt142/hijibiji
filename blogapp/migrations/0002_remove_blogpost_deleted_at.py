# Generated by Django 4.1.4 on 2022-12-20 15:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blogpost',
            name='deleted_at',
        ),
    ]

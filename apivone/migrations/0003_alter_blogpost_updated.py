# Generated by Django 4.1.4 on 2022-12-20 04:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apivone', '0002_city_interests_person_personaddress'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='updated',
            field=models.DateTimeField(auto_now=True, null=True, verbose_name='Updated Date'),
        ),
    ]

# Generated by Django 3.2.13 on 2022-05-21 19:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0002_auto_20220521_1621'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='viewingrequest',
            options={'ordering': ['-request_date']},
        ),
    ]
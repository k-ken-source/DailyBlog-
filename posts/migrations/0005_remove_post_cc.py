# Generated by Django 2.2 on 2020-08-03 02:37

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0004_auto_20200729_1934'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='CC',
        ),
    ]

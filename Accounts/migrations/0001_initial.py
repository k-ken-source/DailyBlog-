# Generated by Django 2.2 on 2020-07-29 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=200, unique=True, verbose_name='Username')),
                ('profile', models.ImageField(default='profile.jpg', upload_to='', verbose_name='Profile Picture')),
                ('background', models.ImageField(default='Background.jpg', upload_to='', verbose_name='Background Picture')),
                ('About', models.TextField(default='Add Information About Yourself Here!', verbose_name='About')),
                ('active', models.BooleanField(default=True)),
                ('staff', models.BooleanField(default=False)),
                ('admin', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]

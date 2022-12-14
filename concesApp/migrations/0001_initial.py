# Generated by Django 4.0.3 on 2022-06-07 22:03

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app1', '0015_alter_car_fiscalpower'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='title of message.', max_length=120)),
                ('description', models.TextField(help_text=' write more informations about your car ...', max_length=500)),
                ('time', models.DateTimeField(default=datetime.datetime.now)),
                ('carToBePublished', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app1.car', verbose_name='car')),
            ],
        ),
    ]

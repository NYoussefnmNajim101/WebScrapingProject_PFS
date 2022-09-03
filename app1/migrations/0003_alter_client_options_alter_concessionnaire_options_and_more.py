# Generated by Django 4.0.3 on 2022-05-05 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_car_remove_concessionnaire_birth_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='client',
            options={'verbose_name': 'Client', 'verbose_name_plural': 'Clients'},
        ),
        migrations.AlterModelOptions(
            name='concessionnaire',
            options={'verbose_name': 'Concessionnaire', 'verbose_name_plural': 'Concessionnaires'},
        ),
        migrations.AddField(
            model_name='car',
            name='description',
            field=models.TextField(default='write something', verbose_name='write something'),
            preserve_default=False,
        ),
    ]
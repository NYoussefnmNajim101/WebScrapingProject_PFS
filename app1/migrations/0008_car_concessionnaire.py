# Generated by Django 4.0.3 on 2022-05-14 11:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0007_remove_car_concessionnaire'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='concessionnaire',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.concessionnaire', verbose_name='concessionnaire'),
            preserve_default=False,
        ),
    ]
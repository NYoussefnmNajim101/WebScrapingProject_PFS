# Generated by Django 4.0.4 on 2022-06-03 21:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0013_alter_car_category_alter_car_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='car',
            name='category',
            field=models.CharField(max_length=250, null=True, verbose_name='cat'),
        ),
        migrations.AlterField(
            model_name='car',
            name='color',
            field=models.CharField(max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='dateOfPub',
            field=models.CharField(max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='fiscalPower',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='fuel',
            field=models.CharField(max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='gearbox',
            field=models.CharField(max_length=220, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='marque',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='car',
            name='mileage',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='car',
            name='model',
            field=models.CharField(max_length=250, null=True),
        ),
        migrations.AlterField(
            model_name='car',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.AlterField(
            model_name='car',
            name='price',
            field=models.CharField(max_length=250),
        ),
        migrations.DeleteModel(
            name='ForeignCar',
        ),
    ]
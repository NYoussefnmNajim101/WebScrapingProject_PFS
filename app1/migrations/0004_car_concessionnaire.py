# Generated by Django 4.0.3 on 2022-05-05 12:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_client_options_alter_concessionnaire_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='car',
            name='concessionnaire',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='app1.concessionnaire', verbose_name='concessionnaire'),
            preserve_default=False,
        ),
    ]
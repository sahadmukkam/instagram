# Generated by Django 3.1.5 on 2021-02-03 06:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210203_1131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccounts',
            name='firstname',
            field=models.CharField(default='', max_length=40),
        ),
        migrations.AlterField(
            model_name='useraccounts',
            name='lastname',
            field=models.CharField(default='', max_length=40),
        ),
    ]
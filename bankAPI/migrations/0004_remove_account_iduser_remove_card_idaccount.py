# Generated by Django 4.2.4 on 2023-08-04 18:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bankAPI', '0003_account_userid_card_accountid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='idUser',
        ),
        migrations.RemoveField(
            model_name='card',
            name='idAccount',
        ),
    ]
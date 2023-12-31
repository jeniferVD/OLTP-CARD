# Generated by Django 4.2.4 on 2023-08-04 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('accountNumber', models.IntegerField(null=True)),
                ('accountType', models.CharField(max_length=1, null=True)),
                ('balance', models.FloatField(null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('idUser', models.IntegerField(verbose_name='bankAPI.User')),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardNumber', models.IntegerField(null=True)),
                ('createdAt', models.DateTimeField(auto_now_add=True, null=True)),
                ('holder', models.TextField(null=True)),
                ('idAccount', models.IntegerField(verbose_name='bankAPI.Account')),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(null=True)),
                ('lastName', models.TextField(null=True)),
                ('address', models.TextField(null=True)),
                ('phoneNumber', models.TextField(null=True)),
                ('birthDate', models.TextField(null=True)),
                ('email', models.TextField(null=True)),
                ('genre', models.CharField(max_length=1, null=True)),
            ],
        ),
    ]

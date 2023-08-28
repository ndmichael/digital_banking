# Generated by Django 4.2.3 on 2023-08-26 20:01

import clients.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Investment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Savings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pin', models.CharField(blank=True, max_length=4, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='savings', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='FixedDeposit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(blank=True, max_length=20, null=True)),
                ('balance', models.DecimalField(decimal_places=2, max_digits=10)),
                ('pin', models.CharField(blank=True, max_length=4, null=True)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('int_type', models.CharField(choices=[('monthly', 'MONTHLY'), ('yearly', 'YEARLY')], default='gold', max_length=10)),
                ('duration', models.DateField(default=clients.models.today)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='fixeddeposit', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Card',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardtype', models.CharField(choices=[('gold', 'GOLD'), ('infinite', 'INFINITE'), ('platinum', 'PLATINUM')], default='gold', max_length=10)),
                ('number', models.CharField(blank=True, max_length=16, null=True)),
                ('cvv', models.CharField(blank=True, max_length=3, null=True)),
                ('zipcode', models.CharField(blank=True, max_length=7, null=True)),
                ('status', models.BooleanField(default=True)),
                ('address', models.TextField()),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
    ]
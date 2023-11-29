# Generated by Django 4.2.3 on 2023-11-28 14:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0013_alter_transaction_reference_alter_transaction_status_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='card',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='client_cards', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='transaction',
            name='reference',
            field=models.CharField(default='16F1A7C2286', max_length=15),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='reference',
            field=models.CharField(default='B38BCF9A574', max_length=15),
        ),
        migrations.CreateModel(
            name='CardRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardtype', models.CharField(choices=[('gold', 'GOLD'), ('infinite', 'INFINITE'), ('platinum', 'PLATINUM')], default='gold', max_length=10)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='card_request', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
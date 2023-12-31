# Generated by Django 4.2.3 on 2023-11-30 15:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0018_alter_transaction_reference_alter_transfer_reference_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reference',
            field=models.CharField(default='B0D2376AD57', max_length=15),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='reference',
            field=models.CharField(default='4916513EB9E', max_length=15),
        ),
        migrations.CreateModel(
            name='CardRequest',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cardtype', models.CharField(choices=[('gold', 'GOLD'), ('infinite', 'INFINITE'), ('platinum', 'PLATINUM')], default='gold', max_length=10)),
                ('date', models.DateTimeField(default=django.utils.timezone.now)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='card_request', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]

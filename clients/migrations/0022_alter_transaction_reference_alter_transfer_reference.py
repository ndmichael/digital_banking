# Generated by Django 4.2.3 on 2024-12-10 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0021_alter_transaction_reference_alter_transfer_reference'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reference',
            field=models.CharField(default='7492CEBA364', max_length=15),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='reference',
            field=models.CharField(max_length=15, unique=True),
        ),
    ]

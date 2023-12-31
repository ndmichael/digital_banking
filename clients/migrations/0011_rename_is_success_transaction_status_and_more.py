# Generated by Django 4.2.3 on 2023-09-08 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0010_transaction_reference_alter_transfer_reference'),
    ]

    operations = [
        migrations.RenameField(
            model_name='transaction',
            old_name='is_success',
            new_name='status',
        ),
        migrations.RenameField(
            model_name='transfer',
            old_name='is_success',
            new_name='status',
        ),
        migrations.AlterField(
            model_name='transaction',
            name='reference',
            field=models.CharField(default='3AF8264D528', max_length=15),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='reference',
            field=models.CharField(default='59BD23105DE', max_length=15),
        ),
    ]

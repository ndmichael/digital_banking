# Generated by Django 4.2.3 on 2023-08-31 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0008_transaction_is_success'),
    ]

    operations = [
        migrations.AddField(
            model_name='transfer',
            name='description',
            field=models.CharField(default='', max_length=150),
        ),
    ]
# Generated by Django 4.2.3 on 2023-11-30 14:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clients', '0015_rename_created_cardrequest_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='reference',
            field=models.CharField(default='7E055ED77D5', max_length=15),
        ),
        migrations.AlterField(
            model_name='transfer',
            name='reference',
            field=models.CharField(default='57A1A7E26DC', max_length=15),
        ),
    ]

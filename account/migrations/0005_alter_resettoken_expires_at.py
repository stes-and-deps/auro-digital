# Generated by Django 4.1.7 on 2023-05-15 17:29

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_alter_resettoken_expires_at'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resettoken',
            name='expires_at',
            field=models.DateTimeField(default=datetime.datetime(2023, 5, 15, 18, 29, 33, 905557, tzinfo=datetime.timezone.utc)),
        ),
    ]
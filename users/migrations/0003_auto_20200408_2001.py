# Generated by Django 3.0.5 on 2020-04-08 20:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_token_last_used'),
    ]

    operations = [
        migrations.AlterField(
            model_name='token',
            name='last_used',
            field=models.DateTimeField(auto_now=True),
        ),
    ]

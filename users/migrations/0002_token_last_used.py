# Generated by Django 3.0.5 on 2020-04-07 22:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='token',
            name='last_used',
            field=models.DateField(auto_now=True),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-31 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pong', '0009_tournament_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='tournametplaceholder',
            name='round',
            field=models.IntegerField(default=0),
        ),
    ]
# Generated by Django 5.0.4 on 2024-06-23 17:18

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pong', '0017_localtournament_match_localtournament'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tournamentroomname',
            name='user1',
        ),
        migrations.RemoveField(
            model_name='tournamentroomname',
            name='user2',
        ),
        migrations.AddField(
            model_name='tournamentroomname',
            name='alias1',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='tournamentroomname',
            name='alias2',
            field=models.CharField(default='None', max_length=255),
        ),
        migrations.AddField(
            model_name='tournamentroomname',
            name='created_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='tournamentroomname',
            name='friendly',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='tournamentroomname',
            name='opponent',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='roomtournament', to=settings.AUTH_USER_MODEL),
        ),
    ]

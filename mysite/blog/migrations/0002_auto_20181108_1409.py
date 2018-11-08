# Generated by Django 2.1.1 on 2018-11-08 14:09

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='creat_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 8, 14, 9, 54, 817144, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='blog.Post'),
        ),
        migrations.AlterField(
            model_name='post',
            name='creat_date',
            field=models.DateTimeField(default=datetime.datetime(2018, 11, 8, 14, 9, 54, 816734, tzinfo=utc)),
        ),
    ]

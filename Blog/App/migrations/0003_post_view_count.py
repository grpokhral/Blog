# Generated by Django 2.2.10 on 2020-04-24 08:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_post_featured'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='view_count',
            field=models.IntegerField(default=0),
        ),
    ]

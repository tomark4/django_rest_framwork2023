# Generated by Django 4.1.7 on 2023-03-22 00:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='order',
            field=models.IntegerField(default=0),
        ),
    ]

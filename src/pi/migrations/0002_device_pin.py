# Generated by Django 4.2 on 2023-04-13 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pi', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='device',
            name='pin',
            field=models.SmallIntegerField(default=0),
            preserve_default=False,
        ),
    ]

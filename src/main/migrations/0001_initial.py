# Generated by Django 4.2 on 2023-04-14 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AccessKey',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('access_to', models.CharField(blank=True, max_length=50, null=True)),
                ('key', models.CharField(blank=True, max_length=40, null=True, unique=True)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('expire', models.DateTimeField(blank=True, null=True)),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
    ]

# Generated by Django 5.0 on 2023-12-23 13:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0003_parthers'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='parthers',
            name='url',
        ),
    ]
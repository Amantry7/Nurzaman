# Generated by Django 5.0 on 2023-12-25 18:11

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('secondary', '0010_alter_advantages1_disc'),
    ]

    operations = [
        migrations.CreateModel(
            name='Advantages2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('logo', models.ImageField(upload_to='advan2_image/', verbose_name='фото')),
                ('title', models.CharField(max_length=255, verbose_name='название')),
                ('disc1', ckeditor.fields.RichTextField(blank=True, null=True, verbose_name='описание')),
            ],
            options={
                'verbose_name': ('преймушества 2',),
                'verbose_name_plural': 'преймушества 2',
            },
        ),
    ]

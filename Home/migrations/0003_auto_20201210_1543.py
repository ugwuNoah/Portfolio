# Generated by Django 3.1.3 on 2020-12-10 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0002_mywork_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='WhatImGoodAt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('description', models.CharField(max_length=255)),
            ],
        ),
        migrations.AlterField(
            model_name='mywork',
            name='image',
            field=models.ImageField(default=True, upload_to=''),
        ),
    ]

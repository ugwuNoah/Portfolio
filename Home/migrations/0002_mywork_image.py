# Generated by Django 3.1.3 on 2020-12-10 14:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='mywork',
            name='image',
            field=models.ImageField(default=True, upload_to='MYWork'),
        ),
    ]

# Generated by Django 3.1.3 on 2021-02-18 13:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0003_auto_20201210_1543'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mywork',
            name='image',
            field=models.ImageField(default=False, upload_to=''),
        ),
    ]

# Generated by Django 3.1 on 2020-08-12 08:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('insta', '0009_auto_20200812_1122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='posts/'),
        ),
    ]

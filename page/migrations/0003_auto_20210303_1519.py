# Generated by Django 3.1.7 on 2021-03-03 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page', '0002_auto_20210303_1502'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='author',
            field=models.CharField(max_length=56, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='images',
            field=models.ImageField(blank=True, upload_to='images/blog'),
        ),
    ]
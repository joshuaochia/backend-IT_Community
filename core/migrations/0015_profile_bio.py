# Generated by Django 3.1.7 on 2021-03-07 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0014_remove_user_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='bio',
            field=models.CharField(default='Tell us who you are.', max_length=256),
        ),
    ]
# Generated by Django 3.1.7 on 2021-03-07 09:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0015_profile_bio'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='full_name',
            field=models.CharField(default=1, max_length=256),
            preserve_default=False,
        ),
    ]
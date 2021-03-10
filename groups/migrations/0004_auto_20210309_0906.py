# Generated by Django 3.1.7 on 2021-03-09 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_auto_20210309_0859'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
            ],
        ),
        migrations.RemoveField(
            model_name='grouppost',
            name='category',
        ),
        migrations.AddField(
            model_name='grouppost',
            name='categories',
            field=models.ManyToManyField(to='groups.Category'),
        ),
    ]
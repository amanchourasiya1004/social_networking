# Generated by Django 3.0.2 on 2020-01-27 10:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_auto_20200127_0733'),
    ]

    operations = [
        migrations.AddField(
            model_name='main',
            name='fb',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AddField(
            model_name='main',
            name='link',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AddField(
            model_name='main',
            name='set_name',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AddField(
            model_name='main',
            name='tell',
            field=models.CharField(default='-', max_length=12),
        ),
        migrations.AddField(
            model_name='main',
            name='tw',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AddField(
            model_name='main',
            name='yt',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='main',
            name='name',
            field=models.CharField(max_length=20),
        ),
    ]

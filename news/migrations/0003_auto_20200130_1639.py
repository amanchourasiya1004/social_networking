# Generated by Django 3.0.2 on 2020-01-30 16:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0002_auto_20200127_1159'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='news',
            name='Name',
        ),
        migrations.RemoveField(
            model_name='news',
            name='set_name',
        ),
        migrations.AddField(
            model_name='news',
            name='catname',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='news',
            name='name',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AddField(
            model_name='news',
            name='tags',
            field=models.CharField(default='-', max_length=30),
        ),
        migrations.AddField(
            model_name='news',
            name='views',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='news',
            name='body_txt',
            field=models.TextField(default='-'),
        ),
        migrations.AlterField(
            model_name='news',
            name='date',
            field=models.CharField(default='-', max_length=12),
        ),
        migrations.AlterField(
            model_name='news',
            name='pic',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='news',
            name='short_txt',
            field=models.CharField(default='-', max_length=20),
        ),
        migrations.AlterField(
            model_name='news',
            name='writer',
            field=models.CharField(default='-', max_length=30),
        ),
    ]

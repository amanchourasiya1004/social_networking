# Generated by Django 3.0.2 on 2020-02-07 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0006_news_catid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='name',
            field=models.TextField(default='-'),
        ),
    ]
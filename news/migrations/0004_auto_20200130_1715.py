# Generated by Django 3.0.2 on 2020-01-30 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20200130_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='news',
            name='short_txt',
            field=models.TextField(default='-'),
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-27 07:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_main_about'),
    ]

    operations = [
        migrations.AlterField(
            model_name='main',
            name='about',
            field=models.TextField(),
        ),
    ]

# Generated by Django 3.0.2 on 2020-01-27 11:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='test',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=20)),
                ('short_txt', models.CharField(max_length=20)),
                ('body_txt', models.TextField()),
                ('date', models.CharField(max_length=12)),
                ('pic', models.CharField(max_length=20)),
                ('writer', models.CharField(max_length=30)),
                ('set_name', models.CharField(max_length=10)),
            ],
        ),
    ]
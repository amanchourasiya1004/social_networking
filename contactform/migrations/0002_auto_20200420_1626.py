# Generated by Django 3.0.2 on 2020-04-20 16:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('contactform', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='message',
            new_name='msg',
        ),
    ]

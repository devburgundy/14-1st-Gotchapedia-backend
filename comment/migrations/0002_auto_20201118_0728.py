# Generated by Django 3.1.3 on 2020-11-18 07:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comment', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='like',
            old_name='commnet',
            new_name='comment',
        ),
    ]
# Generated by Django 3.2.5 on 2021-10-09 19:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='caption',
            new_name='tag',
        ),
    ]

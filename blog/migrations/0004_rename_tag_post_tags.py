# Generated by Django 3.2.5 on 2021-10-09 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_data_post_date'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='tag',
            new_name='tags',
        ),
    ]
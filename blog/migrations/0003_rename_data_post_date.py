# Generated by Django 3.2.5 on 2021-10-09 19:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_rename_caption_post_tag'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='data',
            new_name='date',
        ),
    ]

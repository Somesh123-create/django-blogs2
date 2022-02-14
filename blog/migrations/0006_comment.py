# Generated by Django 3.2.5 on 2021-10-14 21:39

from django.db import migrations, models
import django.db.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20211015_0148'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=120)),
                ('user_email', models.EmailField(max_length=254)),
                ('text', models.TextField()),
                ('post', models.ForeignKey(on_delete=django.db.models.fields.CharField, related_name='comments', to='blog.post')),
            ],
        ),
    ]
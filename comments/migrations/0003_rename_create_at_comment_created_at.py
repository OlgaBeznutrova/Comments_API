# Generated by Django 4.0.1 on 2022-04-21 21:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0002_comment_create_at'),
    ]

    operations = [
        migrations.RenameField(
            model_name='comment',
            old_name='create_at',
            new_name='created_at',
        ),
    ]

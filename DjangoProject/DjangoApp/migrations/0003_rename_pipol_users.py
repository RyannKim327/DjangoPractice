# Generated by Django 4.2 on 2023-06-21 21:48

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0002_rename_users_pipol'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='pipol',
            new_name='users',
        ),
    ]

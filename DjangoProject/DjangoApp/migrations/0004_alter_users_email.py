# Generated by Django 4.2 on 2023-06-21 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('DjangoApp', '0003_rename_pipol_users'),
    ]

    operations = [
        migrations.AlterField(
            model_name='users',
            name='email',
            field=models.CharField(default='', max_length=50),
        ),
    ]

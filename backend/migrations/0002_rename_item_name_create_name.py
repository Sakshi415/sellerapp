# Generated by Django 4.1.4 on 2022-12-11 15:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='create',
            old_name='item_name',
            new_name='name',
        ),
    ]

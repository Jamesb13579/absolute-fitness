# Generated by Django 3.2 on 2022-11-19 01:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0007_rename_memberships_category'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='membership',
            new_name='category',
        ),
    ]

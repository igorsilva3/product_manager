# Generated by Django 2.2 on 2020-09-03 22:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='categories',
            new_name='categorie',
        ),
    ]

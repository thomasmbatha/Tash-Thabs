# Generated by Django 3.2.12 on 2024-06-30 18:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_comment'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='featured',
            new_name='living',
        ),
    ]

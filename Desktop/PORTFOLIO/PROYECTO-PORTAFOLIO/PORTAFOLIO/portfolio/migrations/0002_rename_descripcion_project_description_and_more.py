# Generated by Django 5.0.4 on 2024-04-06 01:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='project',
            old_name='descripcion',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='project',
            old_name='titulo',
            new_name='title',
        ),
    ]

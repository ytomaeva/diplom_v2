# Generated by Django 4.1.2 on 2023-05-03 08:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_rename_numder_variants_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='variants',
            old_name='L01',
            new_name='L1',
        ),
        migrations.RenameField(
            model_name='variants',
            old_name='R01',
            new_name='R1',
        ),
    ]

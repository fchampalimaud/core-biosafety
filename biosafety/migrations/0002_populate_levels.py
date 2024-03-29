# Generated by Django 2.1.1 on 2018-10-23 14:06

from django.db import migrations


def populate_levels(apps, schema_editor):
    Level = apps.get_model('biosafety', 'Level')

    Level(code='BSL 1', label='Level 1').save()
    Level(code='BSL 2', label='Level 2').save()
    Level(code='BSL 3', label='Level 3').save()
    Level(code='BSL 4', label='Level 4').save()


class Migration(migrations.Migration):

    dependencies = [
        ('biosafety', '0001_initial'),
    ]

    operations = [
        migrations.RunPython(
            populate_levels,
            migrations.RunPython.noop,
        ),
    ]
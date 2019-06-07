# Generated by Django 2.2.1 on 2019-06-07 08:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='Level code')),
                ('label', models.CharField(max_length=255, verbose_name='Small description')),
            ],
        ),
        migrations.CreateModel(
            name='Risk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, verbose_name='Risk code')),
                ('label', models.CharField(max_length=255, verbose_name='Short description')),
                ('url', models.URLField(blank=True, null=True, verbose_name='URL')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
    ]

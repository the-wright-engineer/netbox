# Generated by Django 3.1 on 2020-08-21 19:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('extras', '0050_migrate_customfieldvalues'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CustomFieldValue',
        ),
    ]
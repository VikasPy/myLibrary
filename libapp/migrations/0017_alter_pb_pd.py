# Generated by Django 4.2.2 on 2023-07-25 05:17

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0016_fpd_alter_pb_fpd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pb',
            name='pd',
            field=ckeditor.fields.RichTextField(),
        ),
    ]

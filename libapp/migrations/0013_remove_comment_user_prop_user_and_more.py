# Generated by Django 4.2.2 on 2023-07-20 10:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0012_comment_user_prop_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='comment_user',
            name='prop_user',
        ),
        migrations.AlterField(
            model_name='comment_user',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libapp.profile'),
        ),
    ]

# Generated by Django 4.2.2 on 2023-07-20 09:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('libapp', '0010_alter_book_table_publish_date_comment_user'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment_user',
            name='c_data',
            field=models.DateTimeField(auto_now_add=True, default=2),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='comment_user',
            name='user',
            field=models.CharField(max_length=100),
        ),
    ]

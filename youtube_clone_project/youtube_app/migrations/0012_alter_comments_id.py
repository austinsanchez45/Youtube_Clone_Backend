# Generated by Django 3.2.9 on 2021-11-29 08:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('youtube_app', '0011_remove_comments_commentid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comments',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]

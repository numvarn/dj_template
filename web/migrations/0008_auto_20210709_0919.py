# Generated by Django 3.2.5 on 2021-07-09 09:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_article_reporter'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Article',
        ),
        migrations.DeleteModel(
            name='Reporter',
        ),
    ]
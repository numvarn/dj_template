# Generated by Django 3.2.5 on 2021-07-06 06:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_blog_category'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blog',
            name='category',
            field=models.IntegerField(choices=[(1, 'ข่าวประกาศ'), (2, 'โฆษณา'), (3, 'บันทึก')], default=1),
        ),
    ]
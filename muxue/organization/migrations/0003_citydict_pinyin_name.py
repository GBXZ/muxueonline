# Generated by Django 2.0.7 on 2018-09-16 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organization', '0002_auto_20180827_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='citydict',
            name='pinyin_name',
            field=models.CharField(default='', max_length=40, verbose_name='城市拼音'),
        ),
    ]

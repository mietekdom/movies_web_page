# Generated by Django 2.1.4 on 2019-01-09 20:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20190109_2038'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='imbd_rating',
            new_name='imdb_rating',
        ),
    ]
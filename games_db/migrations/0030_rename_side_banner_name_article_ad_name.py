# Generated by Django 3.2.6 on 2021-10-06 17:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('games_db', '0029_emaillist'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='side_banner_name',
            new_name='ad_name',
        ),
    ]

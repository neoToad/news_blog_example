# Generated by Django 3.2.6 on 2021-08-20 14:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_db', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='articlecontent',
            name='image_credit',
            field=models.CharField(blank=True, default='', max_length=125, null=True),
        ),
    ]

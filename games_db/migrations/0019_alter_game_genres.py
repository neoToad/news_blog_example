# Generated by Django 3.2.6 on 2021-08-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_db', '0018_auto_20210830_0920'),
    ]

    operations = [
        migrations.AlterField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(blank=True, to='games_db.Genre'),
        ),
    ]

# Generated by Django 3.2.6 on 2021-08-27 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_db', '0014_alter_game_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='fb_image',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]

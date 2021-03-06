# Generated by Django 3.2.6 on 2021-08-30 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_db', '0017_alter_article_games'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='games',
            field=models.ManyToManyField(blank=True, to='games_db.Game'),
        ),
        migrations.AlterField(
            model_name='game',
            name='genres',
            field=models.ManyToManyField(to='games_db.Genre'),
        ),
    ]

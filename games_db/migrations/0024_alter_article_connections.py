# Generated by Django 3.2.6 on 2021-08-30 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_db', '0023_alter_article_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='connections',
            field=models.ManyToManyField(blank=True, to='games_db.Connection'),
        ),
    ]

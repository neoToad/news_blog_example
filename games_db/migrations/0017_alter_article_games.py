# Generated by Django 3.2.6 on 2021-08-30 13:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_db', '0016_alter_article_fb_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='games',
            field=models.ManyToManyField(blank=True, null=True, to='games_db.Game'),
        ),
    ]

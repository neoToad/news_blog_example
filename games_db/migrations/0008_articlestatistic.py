# Generated by Django 3.2.6 on 2021-08-24 18:21

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('games_db', '0007_remove_article_genres'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArticleStatistic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(default=django.utils.timezone.now, verbose_name='Date')),
                ('views', models.IntegerField(default=0, verbose_name='Views')),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='games_db.article')),
            ],
        ),
    ]
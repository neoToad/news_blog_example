# Generated by Django 3.2.6 on 2021-08-30 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('games_db', '0020_auto_20210830_1130'),
    ]

    operations = [
        migrations.CreateModel(
            name='Connection',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True, max_length=3000, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='connections',
            field=models.ManyToManyField(to='games_db.Connection'),
        ),
    ]
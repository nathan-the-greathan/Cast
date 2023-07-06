# Generated by Django 4.2.3 on 2023-07-06 01:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('forecast', '0002_tag_remove_newspost_tags_newspost_tags'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newspost',
            name='tags',
        ),
        migrations.AddField(
            model_name='tag',
            name='news_posts',
            field=models.ManyToManyField(related_name='tags', to='forecast.newspost'),
        ),
    ]

# Generated by Django 3.2.14 on 2022-08-17 03:43

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='add keyword for the page to improve seo', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]

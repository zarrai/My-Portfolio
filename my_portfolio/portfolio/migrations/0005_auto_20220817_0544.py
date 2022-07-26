# Generated by Django 3.2.14 on 2022-08-17 03:44

from django.db import migrations
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0005_auto_20220424_2025'),
        ('portfolio', '0004_alter_project_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='project',
            name='tools',
        ),
        migrations.AddField(
            model_name='project',
            name='tags',
            field=taggit.managers.TaggableManager(blank=True, help_text='add keyword for the page to improve seo', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
    ]

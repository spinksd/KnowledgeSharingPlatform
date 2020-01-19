# Generated by Django 3.0.2 on 2020-01-17 19:43

from django.db import migrations, models
import taggit.managers


class Migration(migrations.Migration):

    dependencies = [
        ('taggit', '0003_taggeditem_add_unique_index'),
        ('website', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='content',
            new_name='main_text',
        ),
        migrations.AddField(
            model_name='page',
            name='short_description',
            field=models.CharField(blank=True, max_length=300),
        ),
        migrations.AddField(
            model_name='page',
            name='tags',
            field=taggit.managers.TaggableManager(help_text='A comma-separated list of tags.', through='taggit.TaggedItem', to='taggit.Tag', verbose_name='Tags'),
        ),
        migrations.AlterField(
            model_name='page',
            name='title',
            field=models.CharField(max_length=50),
        ),
    ]

# Generated by Django 3.0.3 on 2020-02-13 19:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_auto_20200211_1749'),
    ]

    operations = [
        migrations.RenameField(
            model_name='page',
            old_name='short_description',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='page',
            old_name='main_text',
            new_name='text',
        ),
    ]

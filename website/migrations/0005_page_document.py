# Generated by Django 3.0.2 on 2020-01-19 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_page_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='document',
            field=models.FileField(blank=True, upload_to='documents/'),
        ),
    ]

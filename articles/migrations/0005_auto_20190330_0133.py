# Generated by Django 2.1 on 2019-03-29 20:03

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0004_article_gender'),
    ]

    operations = [
        migrations.RenameField(
            model_name='article',
            old_name='gender',
            new_name='status',
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-15 08:04

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_remove_article_image_url_article_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='article',
            name='date',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
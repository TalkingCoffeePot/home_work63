# Generated by Django 5.0.1 on 2024-01-16 07:33

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('feed', '0002_remove_postmodel_likes_postmodel_likes'),
    ]

    operations = [
        migrations.AddField(
            model_name='postmodel',
            name='date_add',
            field=models.DateField(auto_now_add=True, default=django.utils.timezone.now, verbose_name='Дата публикации'),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.6 on 2024-06-02 11:12

import django.contrib.postgres.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors_app', '0003_remove_quote_tags_delete_tag_quote_tags'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='tags',
            field=django.contrib.postgres.fields.ArrayField(base_field=models.CharField(max_length=255), blank=True, size=None),
        ),
    ]
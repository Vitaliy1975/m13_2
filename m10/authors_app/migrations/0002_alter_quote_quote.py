# Generated by Django 5.0.6 on 2024-06-02 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authors_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quote',
            name='quote',
            field=models.TextField(),
        ),
    ]
# Generated by Django 5.0.2 on 2024-02-21 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('country_app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='code',
            field=models.CharField(max_length=3),
        ),
    ]

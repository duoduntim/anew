# Generated by Django 5.0.2 on 2024-05-02 04:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_experience_duration'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='duration',
            new_name='period',
        ),
        migrations.AlterField(
            model_name='experience',
            name='description',
            field=models.TextField(max_length=500),
        ),
    ]

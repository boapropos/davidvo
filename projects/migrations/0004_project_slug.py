# Generated by Django 4.0.1 on 2022-01-31 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0003_project_featured_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='slug',
            field=models.SlugField(blank=True),
        ),
    ]

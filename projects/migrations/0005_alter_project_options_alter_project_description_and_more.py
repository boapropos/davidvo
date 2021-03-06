# Generated by Django 4.0.1 on 2022-02-04 21:07

from django.db import migrations, models
import django.db.models.deletion
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('projects', '0004_project_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='project',
            options={'ordering': ('-rank', 'title', 'pk')},
        ),
        migrations.AlterField(
            model_name='project',
            name='description',
            field=tinymce.models.HTMLField(),
        ),
        migrations.AlterField(
            model_name='project',
            name='rank',
            field=models.IntegerField(default=0),
        ),
        migrations.CreateModel(
            name='Credit',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=200)),
                ('name', models.CharField(max_length=200)),
                ('rank', models.IntegerField(default=0)),
                ('url', models.URLField(blank=True)),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='projects.project')),
            ],
        ),
    ]

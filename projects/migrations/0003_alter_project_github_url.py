# Generated by Django 4.2.3 on 2024-05-10 19:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("projects", "0002_alter_project_github_url"),
    ]

    operations = [
        migrations.AlterField(
            model_name="project",
            name="github_url",
            field=models.URLField(),
        ),
    ]

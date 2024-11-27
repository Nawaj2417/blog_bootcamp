# Generated by Django 5.1 on 2024-11-13 18:07

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("Blog", "0005_remove_blog_tags"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blog",
            name="slug",
            field=autoslug.fields.AutoSlugField(
                default=None,
                editable=False,
                null=True,
                populate_from="title",
                unique=True,
            ),
        ),
    ]

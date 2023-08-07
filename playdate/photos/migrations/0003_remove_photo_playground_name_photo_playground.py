# Generated by Django 4.2.3 on 2023-08-07 10:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("playgrounds", "0004_delete_photo"),
        ("photos", "0002_alter_photo_description"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="photo",
            name="playground_name",
        ),
        migrations.AddField(
            model_name="photo",
            name="playground",
            field=models.ForeignKey(
                blank=True,
                default=5,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="photos",
                to="playgrounds.playground",
            ),
            preserve_default=False,
        ),
    ]

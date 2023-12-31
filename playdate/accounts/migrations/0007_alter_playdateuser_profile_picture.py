# Generated by Django 4.2.3 on 2023-08-06 19:10

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("accounts", "0006_alter_playdateuser_profile_picture"),
    ]

    operations = [
        migrations.AlterField(
            model_name="playdateuser",
            name="profile_picture",
            field=models.ImageField(
                blank=True,
                default="/static/images/person02.svg",
                null=True,
                upload_to="profile_picture/",
            ),
        ),
    ]

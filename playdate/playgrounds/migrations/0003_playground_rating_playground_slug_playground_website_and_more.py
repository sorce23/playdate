# Generated by Django 4.2.3 on 2023-07-31 09:45

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("playgrounds", "0002_remove_photo_user"),
    ]

    operations = [
        migrations.AddField(
            model_name="playground",
            name="rating",
            field=models.IntegerField(
                blank=True,
                choices=[
                    (1, "VERY_POOR"),
                    (2, "POOR"),
                    (3, "MEDIOCRE"),
                    (4, "GOOD"),
                    (5, "VERY_GOOD"),
                    (6, "PERFECT"),
                ],
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="playground",
            name="slug",
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name="playground",
            name="website",
            field=models.URLField(blank=True, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name="playground",
            name="address",
            field=models.CharField(
                max_length=200,
                validators=[django.core.validators.MinLengthValidator(3)],
            ),
        ),
        migrations.AlterField(
            model_name="playground",
            name="country",
            field=models.IntegerField(
                choices=[
                    (1, "ALBANIA"),
                    (2, "ANDORRA"),
                    (3, "AUSTRIA"),
                    (4, "BELARUS"),
                    (5, "BELGIUM"),
                    (6, "BOSNIA_AND_HERZEGOVINA"),
                    (7, "BULGARIA"),
                    (8, "CROATIA"),
                    (9, "CYPRUS"),
                    (10, "CZECH_REPUBLIC"),
                    (11, "DENMARK"),
                    (12, "ESTONIA"),
                    (13, "FINLAND"),
                    (14, "FRANCE"),
                    (15, "GERMANY"),
                    (16, "GREECE"),
                    (17, "HUNGARY"),
                    (18, "ICELAND"),
                    (19, "IRELAND"),
                    (20, "ITALY"),
                    (21, "KOSOVO"),
                    (22, "LATVIA"),
                    (23, "LIECHTENSTEIN"),
                    (24, "LITHUANIA"),
                    (25, "LUXEMBOURG"),
                    (26, "MALTA"),
                    (27, "MOLDOVA"),
                    (28, "MONACO"),
                    (29, "MONTENEGRO"),
                    (30, "NETHERLANDS"),
                    (31, "NORTH_MACEDONIA"),
                    (32, "NORWAY"),
                    (33, "POLAND"),
                    (34, "PORTUGAL"),
                    (35, "ROMANIA"),
                    (36, "RUSSIA"),
                    (37, "SAN_MARINO"),
                    (38, "SERBIA"),
                    (39, "SLOVAKIA"),
                    (40, "SLOVENIA"),
                    (41, "SPAIN"),
                    (42, "SWEDEN"),
                    (43, "SWITZERLAND"),
                    (44, "UKRAINE"),
                    (45, "UNITED_KINGDOM"),
                    (46, "VATICAN_CITY"),
                ]
            ),
        ),
        migrations.AlterField(
            model_name="playground",
            name="name",
            field=models.CharField(
                max_length=50, validators=[django.core.validators.MinLengthValidator(2)]
            ),
        ),
    ]

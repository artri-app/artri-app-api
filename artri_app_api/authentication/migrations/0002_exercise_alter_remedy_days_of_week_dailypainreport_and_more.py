# Generated by Django 5.2 on 2025-04-09 16:36

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("authentication", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Exercise",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField()),
                ("tutorial_link", models.URLField()),
                (
                    "difficulty",
                    models.CharField(
                        choices=[
                            ("Easy", "Fácil"),
                            ("Medium", "Médio"),
                            ("Hard", "Difícil"),
                        ],
                        default="Easy",
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="remedy",
            name="days_of_week",
            field=models.CharField(
                choices=[
                    ("Monday", "Segunda-feira"),
                    ("Tuesday", "Terça-feira"),
                    ("Wednesday", "Quarta-feira"),
                    ("Thursday", "Quinta-feira"),
                    ("Friday", "Sexta-feira"),
                    ("Saturday", "Sábado"),
                    ("Sunday", "Domingo"),
                ],
                default="Monday",
                max_length=9,
            ),
        ),
        migrations.CreateModel(
            name="DailyPainReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                ("pain_level", models.IntegerField()),
                ("pain_location", models.CharField(max_length=50)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Training",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=50)),
                ("description", models.TextField()),
                (
                    "difficulty",
                    models.CharField(
                        choices=[
                            ("Easy", "Fácil"),
                            ("Medium", "Médio"),
                            ("Hard", "Difícil"),
                        ],
                        default="Easy",
                    ),
                ),
                ("exercises", models.ManyToManyField(to="authentication.exercise")),
            ],
        ),
        migrations.CreateModel(
            name="TrainingReport",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("date", models.DateField()),
                (
                    "training",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="authentication.training",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

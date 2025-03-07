# Generated by Django 5.0.6 on 2024-07-09 11:38

import django.utils.timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("auth", "0012_alter_user_first_name_max_length"),
    ]

    operations = [
        migrations.CreateModel(
            name="User",
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
                ("password", models.CharField(max_length=128, verbose_name="password")),
                (
                    "last_login",
                    models.DateTimeField(
                        blank=True, null=True, verbose_name="last login"
                    ),
                ),
                (
                    "date_joined",
                    models.DateTimeField(
                        default=django.utils.timezone.now, verbose_name="date joined"
                    ),
                ),
                (
                    "email",
                    models.EmailField(
                        max_length=254, unique=True, verbose_name="почта"
                    ),
                ),
                ("first_name", models.CharField(max_length=30, verbose_name="имя")),
                ("last_name", models.CharField(max_length=150, verbose_name="фамилия")),
                (
                    "phone",
                    models.CharField(
                        blank=True, max_length=35, null=True, verbose_name="телефон"
                    ),
                ),
                (
                    "avatar",
                    models.ImageField(
                        blank=True,
                        null=True,
                        upload_to="users/avatars/",
                        verbose_name="аватар",
                    ),
                ),
                (
                    "is_admin",
                    models.BooleanField(default=False, verbose_name="администратор"),
                ),
                ("town", models.CharField(blank=True, max_length=100, null=True)),
                (
                    "is_active",
                    models.BooleanField(default=True, verbose_name="активность"),
                ),
                (
                    "role",
                    models.CharField(
                        choices=[("user", "USER"), ("admin", "ADMIN")],
                        default="user",
                        max_length=10,
                        verbose_name="роль",
                    ),
                ),
                (
                    "groups",
                    models.ManyToManyField(
                        blank=True,
                        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.group",
                        verbose_name="groups",
                    ),
                ),
                (
                    "user_permissions",
                    models.ManyToManyField(
                        blank=True,
                        help_text="Specific permissions for this user.",
                        related_name="user_set",
                        related_query_name="user",
                        to="auth.permission",
                        verbose_name="user permissions",
                    ),
                ),
            ],
            options={
                "verbose_name": "Пользователь",
                "verbose_name_plural": "Пользователи",
                "ordering": ["email"],
            },
        ),
    ]

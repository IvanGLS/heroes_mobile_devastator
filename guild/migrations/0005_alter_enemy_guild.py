# Generated by Django 4.1.5 on 2023-01-23 14:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guild", "0004_remove_enemy_heroes_enemy_heroes"),
    ]

    operations = [
        migrations.AlterField(
            model_name="enemy",
            name="guild",
            field=models.CharField(max_length=60),
        ),
    ]

# Generated by Django 4.1.5 on 2023-01-22 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guild", "0003_remove_enemy_heroes_enemy_heroes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="enemy",
            name="heroes",
        ),
        migrations.AddField(
            model_name="enemy",
            name="heroes",
            field=models.ManyToManyField(related_name="enemy_hero", to="guild.heroes"),
        ),
    ]

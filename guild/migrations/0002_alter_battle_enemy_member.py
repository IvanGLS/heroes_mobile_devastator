# Generated by Django 4.1.5 on 2023-01-22 14:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("guild", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="battle",
            name="enemy_member",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="battle_enemy",
                to="guild.enemy",
            ),
        ),
    ]
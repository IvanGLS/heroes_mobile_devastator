# Generated by Django 4.1.5 on 2023-01-25 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("guild", "0007_alter_guildmember_heroes"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="guildmember",
            name="heroes",
        ),
        migrations.AddField(
            model_name="enemy",
            name="guild_member_heroes",
            field=models.ManyToManyField(related_name="guild_hero", to="guild.heroes"),
        ),
    ]

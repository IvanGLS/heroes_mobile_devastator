from django.conf import settings
from django.contrib.auth.models import AbstractUser
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.utils import timezone


class Heroes(models.Model):
    name = models.CharField(max_length=60, unique=True)
    image = models.ImageField(upload_to="media/%Y/%m/%d/")

    def __str__(self):
        return "{}".format(self.name)


class GuildMember(AbstractUser):
    power = models.IntegerField(null=True, blank=True)

    class Meta:
        ordering = ["username"]

    def __str__(self):
        return f"{self.username} ({self.first_name} {self.last_name})"


class Enemy(models.Model):
    name = models.CharField(max_length=60, unique=True)
    power = models.IntegerField()
    guild = models.CharField(max_length=60)
    heroes = models.ManyToManyField(Heroes,
                                    related_name="enemy_hero")
    guild_member_heroes = models.ManyToManyField(Heroes,
                                                 related_name="guild_hero")

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return f"{self.name} ({self.guild})"


class Battle(models.Model):
    data = models.DateTimeField(auto_now_add=True)
    guild_member = models.ForeignKey(GuildMember,
                                     on_delete=models.CASCADE,
                                     related_name="battle_guild")
    enemy_member = models.ForeignKey(Enemy,
                                     on_delete=models.CASCADE,
                                     related_name="battle_enemy")

    class Meta:
        ordering = ["-data"]

    def __str__(self):
        return f"{self.guild_member} vs {self.enemy_member}"

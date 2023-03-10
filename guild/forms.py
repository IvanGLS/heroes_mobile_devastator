from django import forms
from django.utils.safestring import mark_safe
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm
from django.core.exceptions import ValidationError
from django.forms import Textarea

from .models import Battle, Enemy, Heroes


class EnemySearchForm(forms.Form):
    title = forms.CharField(
        max_length=255,
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "Search by enemies..."})
    )


class CustomChoiceField(forms.ModelMultipleChoiceField):

    def label_from_instance(self, obj):
        return mark_safe("<img src='%s'/>" % obj.image.url)


class EnemyForm(forms.ModelForm):
    heroes = CustomChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Heroes.objects.all())
    guild_member_heroes = CustomChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Heroes.objects.all())

    class Meta:
        model = Enemy
        fields = "__all__"


class BattleForm(forms.ModelForm):
    guild_member_heroes = CustomChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Heroes.objects.all())

    enemy_member_heroes = CustomChoiceField(
        widget=forms.CheckboxSelectMultiple,
        queryset=Heroes.objects.all())

    class Meta:
        model = Battle
        fields = ("enemy_member", "guild_member_heroes", "enemy_member_heroes")
        labels = {
            "enemy_member": "enemy_member",
            "guild_member_heroes": "guild_member_heroes",
        }

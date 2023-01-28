from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy, reverse
from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404

from django.contrib.auth.mixins import LoginRequiredMixin
import textwrap

from django.views.generic.edit import FormMixin

from .models import Battle, GuildMember, Enemy
from .forms import EnemySearchForm, EnemyForm, BattleForm


class BattleListView(LoginRequiredMixin, generic.ListView):
    model = Battle
    ordering = ["-data"]
    paginate_by = 5
    template_name = "guild/index.html"
    queryset = Battle.objects.all().select_related("enemy_member")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(BattleListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("enemy_member__name", "")

        context["search_form"] = EnemySearchForm(initial={"enemy_member__name": name},)

        return context

    def get_queryset(self):
        queryset = self.queryset
        form = EnemySearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(enemy_member__name__icontains=form.cleaned_data["title"])

        return queryset


class MemberDetailView(LoginRequiredMixin, generic.DetailView):
    model = GuildMember

    def get_success_url(self, **kwargs):
        return reverse_lazy(
            "guild:member-detail",
            kwargs={"pk": self.get_object().id}
        )


class EnemyCreateView(LoginRequiredMixin, generic.CreateView):
    model = Enemy
    form_class = EnemyForm
    success_url = reverse_lazy("guild:enemy-list")


class EnemyUpdateView(LoginRequiredMixin, generic.UpdateView):
    model = Enemy
    form_class = EnemyForm
    success_url = reverse_lazy("guild:enemy-list")


class EnemyListView(LoginRequiredMixin, generic.ListView):
    model = Enemy
    ordering = ["-id"]
    paginate_by = 5
    queryset = Enemy.objects.all().prefetch_related("heroes")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(EnemyListView, self).get_context_data(**kwargs)

        name = self.request.GET.get("name", "")

        context["search_form"] = EnemySearchForm(initial={"name": name},)

        return context

    def get_queryset(self):
        queryset = self.queryset
        form = EnemySearchForm(self.request.GET)

        if form.is_valid():
            return queryset.filter(name__icontains=form.cleaned_data["title"])

        return queryset


@login_required
def battle_remove(request, pk):
    if request.user == Battle.objects.get(pk=pk).guild_member:
        Battle(id=pk).delete()
    return HttpResponseRedirect(reverse_lazy("guild:member-detail", args=[request.user.id]))


@login_required
def enemy_remove(request, pk):
    Enemy(id=pk).delete()
    return HttpResponseRedirect(reverse_lazy("guild:enemy-list"))


@login_required
def add_battle(request, pk):
    enemy = Enemy(id=pk)
    user_battle = Battle.objects.create(guild_member_id=request.user.id, enemy_member_id=enemy.id)
    user_battle.save()
    return HttpResponseRedirect(reverse_lazy("guild:member-detail", args=[request.user.id]))

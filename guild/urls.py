import django
from django.urls import path

from .views import (BattleListView,
                    MemberDetailView,
                    EnemyCreateView,
                    EnemyListView,
                    EnemyUpdateView,
                    battle_remove,
                    enemy_remove,
                    add_battle,
                    )


urlpatterns = [
    path("", BattleListView.as_view(), name="battle-list"),
    path("user/<int:pk>/",
         MemberDetailView.as_view(),
         name="member-detail"),
    path("enemy/", EnemyListView.as_view(), name="enemy-list"),
    path("enemy/create/", EnemyCreateView.as_view(), name="enemy-create"),
    path(
        "battle/<int:pk>/remove/",
        battle_remove,
        name="battle-remove",
        ),
    path(
        "enemy/<int:pk>/update/",
        EnemyUpdateView.as_view(),
        name="enemy-update",),
    path(
        "enemy/<int:pk>/remove/",
        enemy_remove,
        name="enemy-remove",
        ),
    path(
        "battle/<int:pk>/add/",
        add_battle,
        name="battle-add",
        ),
]

app_name = "guild"

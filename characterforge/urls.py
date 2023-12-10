from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    
    path("", views.index, name="index"),
    path('create-character/', views.initailize_character, name='initialize-character'),
    path('create-character/<int:character_id>/race/', views.character_race, name='character-race'),
    path('create-character/<int:character_id>/class/', views.character_class, name='character-class'),
    path('create-character/<int:character_id>/ability_score/', views.character_ability_score, name='character-ability-scores'),
    path('create-character/<int:character_id>/feat/', views.character_feat, name='character-feat'),
    path('create-character/<int:character_id>/alignment/', views.character_alignment, name='character-alignment'),
    path('create-character/<int:character_id>/background/', views.character_background, name='character-background'),
    path('create-character/<int:character_id>/skill/', views.character_skill, name='character-skill'),
    path('create-character/<int:character_id>/proficiency/', views.character_proficiency, name='character-proficiency'),
    path('create-character/<int:character_id>/spell/', views.character_spell, name='character-spell'),
    path('create-character/<int:character_id>/equipment/', views.character_equipment, name='character-equipment'),
    path('create-character/<int:character_id>/item/', views.character_item, name='character-item'),
    path('create-character/<int:character_id>/description/', views.character_description, name='character-description'),
    path("create-character/<int:character_id>/confirm/", views.confirm_character, name="confirm-character"),
    path("create-character/<int:character_id>/edit/", views.character_edit_view, name="edit-character"),
    path("create-character/<int:character_id>/delete/", views.delete_character, name="delete-character"),
    path("create-character/<int:character_id>/detail/", views.character_detail_view, name="character-detail"),
    path("character_list/", views.character_list_view, name="character-list"),
]

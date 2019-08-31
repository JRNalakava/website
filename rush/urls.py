from django.urls import path

from . import views

urlpatterns = [
    path('', views.rush, name='rush'),
    path('apply/<username>', views.apply, name='apply'),
    path('apply/done/<username>', views.done, name='done'),
    path('apply/saved/', views.save, name='save'),
    path('apply/incomplete/<username>', views.incomplete, name='incomplete'),
    path('directory/', views.directory, name='rush_directory'),
    path('directory/account/<username>', views.account, name='rush_account'),
    path('directory/account/<username>/<comment_id>', views.delete, name='delete_comment'),
    path('vote/<username>', views.vote, name='rush_vote'),
    path('vote/<username>/<vote_value>', views.register_vote, name='register_vote'),
]

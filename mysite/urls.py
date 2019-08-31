from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path('directory/', views.directory, name='directory'),
    path('directory/accounts/<user_name>', views.brother_account),
    path('directory/accounts/manage/<user_name>', views.manage_account),
    path('account/', views.account, name='account'),
]

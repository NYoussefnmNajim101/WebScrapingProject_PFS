from django.urls import path
from . import views

urlpatterns=[
    path('',views.home1,name='home1'),
    path('home1/',views.home1,name='home1'),

    path('contact/',views.contact,name='contact'),
    path('login/',views.login,name='login'),
    path('profil/',views.profil,name='profilClient'),
    path('profil/',views.profil,name='profilConss'),
    path('login/inscrire/',views.inscrire,name='inscrire'),
    path('login/inscrire/client',views.inscrireClient,name='inscrireClient'),
    path('search_cars/',views.home1,name='search_cars'),

    path('search_cars_cons/',views.concessionnaire,name='search_cars_cons'),
    path('search_cars_client/',views.client,name='search_cars_client'),
]
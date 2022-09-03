from django.urls import path,include
from . import views
urlpatterns = [
    #path('add', views.addPost, name='add'),
    #path('addcar', views.addCar, name='addCar'),
    path('addcar', views.addCar, name='addCar'),
    path('addcaro', views.addCar1, name='addCaro'),
    path('myPosts',views.concessionnaire,name='myPosts'),
    path('posta', views.concessionnaire1, name='posta'),
    path('update/<int:id>',views.update,name='update'),
    path('update1/<int:id>', views.update1, name='update1'),
    path('delete/<int:id>',views.delete,name='delete'),
    path('delete1/<int:id>', views.delete1, name='delete1'),


]
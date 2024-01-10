from django.urls import path
from . import views

urlpatterns=[
    path('', views.projects, name="projects"),
    path('name/', views.name, name="name"),
    path('word', views.wordcount, name="wordcount"),
    path('counter/',views.counter,name='counter'),
    path('css/',views.css,name='css'),
    path('clubs/',views.clubs,name='clubs'),
    path('create_project/',views.createProject,name='create_project'),
    path('update_project/<str:pk>/',views.updateProject,name='update_project'),
    path('delete_project/<str:pk>/',views.deleteProject,name='delete_project')
]
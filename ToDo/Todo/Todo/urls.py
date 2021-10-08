from django.contrib import admin
from django.urls import path, include

from api import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('help/', include('api.urls')),
    path('tasks/', views.getTasks),
    path('tasks/<str:pk>/', views.getTask),
    path('tasks/create/', views.createTask),
    path('tasks/<str:pk>/update/', views.updateTask),
    path('tasks/<str:pk>/delete/', views.deleteTask),
]

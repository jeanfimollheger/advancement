from django.urls import path
from .views import ProjectListView, ProjectDetailView,ProjectCreateView

app_name = 'todolist'  # Définir l'espace de noms ici

urlpatterns = [
    path('projects_list/', ProjectListView.as_view(), name='projects_list'),
    path('project_detail/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project_creation/', ProjectCreateView.as_view(), name='project_creation'),
]
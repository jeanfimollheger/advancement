from django.urls import path
from .views import ProjectListView, ProjectDetailView,ProjectCreateView, ProjectUpdateView, ProjectDeleteView
from .views import TaskCreateView, TaskListView, TaskDetailView, TaskUpdateView, TaskDeleteView,TaskCalendarView
app_name = 'todolist'  # Définir l'espace de noms ici

urlpatterns = [
    path('projects_list/', ProjectListView.as_view(), name='projects_list'),
    path('project_detail/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),
    path('project_creation/', ProjectCreateView.as_view(), name='project_creation'),
    path('project_update/<str:slug>/', ProjectUpdateView.as_view(), name='project_update'),
    path('project_delete/<str:slug>/', ProjectDeleteView.as_view(), name='project_delete'),
    # Task
    path('task_list/', TaskListView.as_view(), name='task_list'),
    path('task_calendar_list/', TaskCalendarView.as_view(), name='task_calendar_list'),
    path('task_detail/<str:slug>', TaskDetailView.as_view(), name='task_detail'),
    path('task_creation/', TaskCreateView.as_view(), name='task_creation'),
    path('task_update/<str:slug>/', TaskUpdateView.as_view(), name='task_update'),
    path('task_delete/<str:slug>/', TaskDeleteView.as_view(), name='task_delete')
]
from django.urls import path
from .views import ProjectListView

urlpatterns = [
    path('projects_list/', ProjectListView.as_view(), name='projects_list'),
    #path('login/', UserLoginView.as_view(), name='login'),
    #path('logout/', UserLogoutView.as_view(), name='logout'),
]
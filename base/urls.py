from django.urls import path
from . import views


urlpatterns = [
	path('demo', views.home, name='home'),
    path('project/', views.project, name='project'),
]
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("dash/", views.dashboard, name="dashboard"),
    path("create/", views.create_task, name="create_task"),
    # path("dash/", views,dashboard, name='dash')
]

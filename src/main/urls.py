from django.urls import path
from . import views


app_name = 'main'  # here for namespacing of urls.

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("dashboard", views.admin, name="admin"),
    path("teacher", views.teacher, name="teacher"),
    path("tutorials", views.tutorials, name="tutorials"),
    path("libary", views.library, name="library"),
    path("tutorialsSeries", views.tutorialsSeries, name="tutorialsSeries"),
]
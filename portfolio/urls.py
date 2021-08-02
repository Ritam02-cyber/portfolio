from django.urls import path
from . import views
urlpatterns = [
    path("", views.home, name="home"),
    path("single_project/<int:pk>", views.single_project, name="single_project"),
    path("contact", views.contact, name="contact"),
    path("services", views.services, name="services"),
    path("about", views.about, name="about"),
    path("portfolio", views.portfolio, name="portfolio")
]
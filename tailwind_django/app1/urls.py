from django.urls import URLPattern, path
from . import views

urlpatterns = [
    path('', views.home, name='index'),
    path("about/", views.home, name="home"),
    path("home/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("search/<q>", views.searchAjax, name="search"),

]
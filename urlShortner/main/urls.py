from django.urls import path
from . import views

urlpatterns = [
    # Let this be the default home page
    path("", views.index, name="index"),
    path("shorten", views.shorten, name="shorten"),
]

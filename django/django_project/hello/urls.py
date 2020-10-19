from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("pragat", views.pragat, name="pragat"),
    path("<str:name>", views.greet, name="greet")
]

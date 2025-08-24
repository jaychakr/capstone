from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("question", views.question, name="question"),
    path("answer/<int:id>/", views.answer, name="answer"),
]

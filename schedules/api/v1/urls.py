from django.urls import path

from . import views

urlpatterns = [
    path("", views.create_schedule, name="schedule_create"),
    path("<str:user_id>/", views.schedules, name="schedule_list"),
]
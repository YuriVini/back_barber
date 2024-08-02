from django.urls import path, include


urlpatterns = [
    path("api/v1/schedule/", include("schedules.api.v1.urls"), name="schedule"),
]
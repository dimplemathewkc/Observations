from . import views
from django.urls import path

urlpatterns = [
    path(
        "get_observations/",
        views.get_observation_by_name,
        name="get_observations_by_name",
    ),
    path(
        "get_latest_observations/",
        views.get_latest_observation_by_name,
        name="get_latest_observations",
    ),
    path("add_observations/", views.insert_observations, name="insert_observations"),
    path("observation_mean/", views.observation_mean, name="get_observation_mean"),
]

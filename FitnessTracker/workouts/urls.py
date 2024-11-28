from django.urls import path
from . import views


app_name = "workouts"

urlpatterns = [
    path("new/workout/", views.new_workout_view, name="new_workout_view"),
    path("update/<workout_id>/", views.workout_update_view, name="workout_update_view"),
    path("delete/<workout_id>/", views.workout_delete_view, name="workout_delete_view"),
    
    path("sets/new/", views.new_set_view, name="new_set_view"),
    path("sets/update/<set_id>/", views.set_update_view, name="set_update_view"),
    path("sets/delete/<set_id>/", views.set_delete_view, name="set_delete_view"),
    
    path("search/workouts/", views.search_workouts_view, name="search_workouts_view"),
]
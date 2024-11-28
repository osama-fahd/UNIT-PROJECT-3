from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .models import Exercise
from .forms import ExerciseForm


from django.contrib import messages


def all_exercises_view(request:HttpRequest):
    exercises = Exercise.objects.all()
    
    return render(request, "exercises/all_exercises.html", {'exercises': exercises})


def exercise_detail_view(request:HttpRequest, exercise_id:int):
    exercise = Exercise.objects.get(pk=exercise_id)
    
    return render(request, "exercises/exercise_detail.html", {'exercise': exercise})


def new_exercise_view(request:HttpRequest):
    exercise_form = ExerciseForm()
    
    if request.method == "POST":
        exercise_form = ExerciseForm(request.POST, request.FILES)
        if exercise_form.is_valid():
            exercise_form.save()
            messages.success(request, "Added Exercise Successfuly!", "alert-success")
            return redirect("main:home_view")
        else:
            print("not valid form", exercise_form.errors)
            messages.error(request, "Couldn't Add Exercise!", "alert-danger")
    
    return render(request, "exercises/new_exercise.html")


def update_exercise_view(request:HttpRequest, exercise_id:int):
    exercise = Exercise.objects.get(pk=exercise_id)
    
    if request.method == "POST":
        exercise_form = ExerciseForm(instance=exercise, data=request.POST, files=request.FILES)
        if exercise_form.is_valid():
            exercise_form.save()
            messages.success(request, "Updated Exercise Successfuly!", "alert-success")
            return redirect("exercises:exercise_detail_view")
        else:
            print("not valid form", exercise_form.errors)
            messages.error(request, "Couldn't Update Exercise!", "alert-danger")
    
    return render(request, "exercises/update_exercise.html")

def delete_exercise_view(request:HttpRequest,  exercise_id:int):
    try:
        exercise = Exercise.objects.get(pk=exercise_id)
        exercise.delete()
        messages.success(request, "Deleted Exercise Successfuly!", "alert-success")
    except Exception as e:
        print(e)
        messages.error(request, "Couldn't Delete Exercise!", "alert-danger")
    
    return redirect("main:home_view")


def search_exercises_view(request:HttpRequest):
    if "search" in request.GET and len(request.GET["search"]) >= 3:
        exercises = Exercise.objects.filter(name__contains=request.GET["search"])
    
    else:
        messages.error(request, "Couldn't Find Exercise!", "alert-danger")
        exercises = []
    
    return render(request, "exercises/exercise_search.html", {'exercises': exercises,})

    
    
    


    
    
    
from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .forms import RoutineForm
from .models import Routine

from workouts.models import Workout, Set, Check

from exercises.models import Exercise

from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required

from django.db import IntegrityError, transaction



def all_routines_view(request:HttpRequest):
    # exercises = Exercise.objects.all()
    # workouts = Workout.objects.all()
    
    routines = Routine.objects.all()
        
    page_number = request.GET.get("page", 1)
    paginator = Paginator(routines, 4)
    routines_page = paginator.get_page(page_number)
    
    return render(request, "routines/all_routines.html", {
                                                            # 'routines': routines, 
                                                            'routines': routines_page,
                                                            # 'workouts': workouts,
                                                            # 'exercises': exercises,
                                                        })

def routine_detail_view(request:HttpRequest, routine_id:int):
    routine = Routine.objects.get(pk=routine_id)
    
    checks = Check.objects.all()
    
    return render(request, "routines/routine_details.html", {'routine': routine, 'checks': checks})


def new_routine_view(request:HttpRequest):
    routine_form = RoutineForm()
    
    if request.method == "POST":
        routine_form = RoutineForm(request.POST)
        if routine_form.is_valid():
            with transaction.atomic():
                routine = routine_form.save()
                messages.success(request, "Continue To Add Your Workouts!", "alert-success")
                return redirect("workouts:new_workout_view", routine.id)
        else:
            print("not valid form", routine_form.errors)
            messages.error(request, "Couldn't Able To Add The title!", "alert-danger")
    
    return render(request, "routines/new_routine.html", {"routine_form": routine_form})


def update_routine_view(request:HttpRequest, routine_id:int):
    routine = Routine.objects.get(pk=routine_id)
    
    if request.method == "POST":
        routine_form = RoutineForm(instance=routine, data=request.POST)
        if routine_form.is_valid():
            routine_form.save()
            messages.success(request, "Updated Routine Successfully!", "alert-success")
            return redirect("main:home_view")
        else:
            print("not valid form", routine_form.errors)
            messages.error(request, "Couldn't Update Routine!", "alert-danger")
    
    return render(request, "routines/update_routine.html")

def delete_routine_view(request:HttpRequest,  routine_id:int):
    try:
        routine = Routine.objects.get(pk=routine_id)
        routine.delete()
        messages.success(request, "Deleted Routine Successfully!", "alert-success")
    except Exception as e:
        print(e)
        messages.error(request, "Couldn't Delete Routine!", "alert-danger")
    
    return redirect("main:home_view")


def search_routines_view(request:HttpRequest):
    if "search" in request.GET and len(request.GET["search"]) >= 3:
        routines = Routine.objects.filter(name__contains=request.GET["search"])
    
    else:
        messages.error(request, "Couldn't Find Routine!", "alert-danger")
        routines = []
    
    return render(request, "routines/search_routine.html", {'routines': routines,})

    
    
    


    
    
    
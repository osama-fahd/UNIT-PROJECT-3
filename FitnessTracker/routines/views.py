from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .forms import RoutineForm
from .models import Routine

from workouts.forms import WorkoutForm, SetForm
from workouts.models import Workout, Set

from exercises.models import Exercise

from django.contrib import messages
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required



def all_routines_view(request:HttpRequest):
    # exercises = Exercise.objects.all()
    # workouts = Workout.objects.all()
    
    routines = Routine.objects.all()
        
    # page_number = request.GET.get("page", 1)
    # paginator = Paginator(routines, 4)
    # routines_page = paginator.get_page(page_number)
    
    return render(request, "routines/all_routines.html", {
                                                            'routines': routines, 
                                                            # 'routines': routines_page,
                                                            # 'workouts': workouts,
                                                            # 'exercises': exercises,
                                                        })

def routine_detail_view(request:HttpRequest, routine_id:int):
    routine = Routine.objects.get(pk=routine_id)
    
    return render(request, "routines/routine_details.html", {'routine': routine})


def new_routine_view(request:HttpRequest):
    # if request.GET.get('exercise_id'):
    #     exercise_id = request.GET.get('exercise_id')
    #     exercise_id = int(exercise_id)
    #     chosen_exercise = Exercise.objects.get(pk=exercise_id)
    #     chosen_routine = request.GET.get('routine_name')
    # else:
    #     chosen_exercise = ''
    #     chosen_routine = ''
    
    if request.method == 'POST':
        name = request.POST['name']
        routine = Routine.objects.create(name=name)

        exercises = request.POST.getlist('exercise[]')
        notes = request.POST.getlist('note[]')
        rest_times = request.POST.getlist('restTime[]')

        for exercise_id, note, rest_time in zip(exercises, notes, rest_times):
            exercise = Exercise.objects.get(id=exercise_id)
            Workout.objects.create(
                routine=routine,
                exercise=exercise,
                note=note,
                restTime=int(rest_time) if rest_time else None
            )

        return redirect('routines:routine_list')

    exercises = Exercise.objects.all()
    return render(request, 'routines/new_routine.html', {'exercises': exercises,
                                                        #  'chosen_routine': chosen_routine,
                                                        #  'chosen_exercise': chosen_exercise
                                                         })


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

    
    
    


    
    
    
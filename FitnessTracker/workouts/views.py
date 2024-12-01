from django.shortcuts import render, redirect
from django.http import HttpRequest, HttpResponse

from .forms import WorkoutForm
from .models import Workout, Set

from routines.models import Routine

from exercises.models import Exercise

from django.contrib import messages


def new_workout_view(request: HttpRequest, routine_id: int):
    routine = Routine.objects.get(pk=routine_id)
    exercises = Exercise.objects.all()
    
    workout_form = WorkoutForm()

    if request.method == "POST":
        workout_form = WorkoutForm(request.POST)
        if workout_form.is_valid():
            workout = workout_form.save(commit=False)
            if request.POST["restTime"].isdigit():
                workout.restTime = int(request.POST["restTime"])
                workout.routine = routine
                workout.save()
                if request.POST.get("repetition", "").strip():
                    if request.POST['repetition'].isdigit():
                        weight = request.POST["weight"]
                        try:
                            weight = float(weight) 
                            if weight <= 0:
                                messages.error(request, "Weight must be a positive number.", "alert-danger")
                            else:
                                new_set = Set(weight=weight, repetition=int(request.POST['repetition']), workout=workout)
                                new_set.save()
                        except ValueError:
                            messages.error(request, "Weight must be a valid number.", "alert-danger")

                
                messages.success(request, "Workout added successfully!", "alert-success")
                return redirect("routines:routine_detail_view", routine_id=routine_id)
            else:
                messages.error(request, "Couldn't save the workout. Please correct the errors.", "alert-danger")
            
        else:
            messages.error(request, "Couldn't save the workout. Please correct the errors.", "alert-danger")

    return render(
        request,"workouts/new_workout.html",
        {
            "routine": routine,
            'exercises': exercises,
        },
    )


def update_workout_view(request:HttpRequest, workout_id:int):
    workout = Workout.objects.get(pk=workout_id)
    
    if request.method == "POST":
        workout_form = WorkoutForm(instance=workout, data=request.POST)
        if workout_form.is_valid():
            workout_form.save()
            messages.success(request, "Updated Workout Successfuly!", "alert-success")
            return redirect("main:home_view")
        else:
            print("not valid form", workout_form.errors)
            messages.error(request, "Couldn't Update Workout!", "alert-danger")
    
    return render(request, "workouts/update_workout.html")

def delete_workout_view(request:HttpRequest,  workout_id:int):
    try:
        workout = Workout.objects.get(pk=workout_id)
        workout.delete()
        messages.success(request, "Deleted Workout Successfuly!", "alert-success")
    except Exception as e:
        print(e)
        messages.error(request, "Couldn't Delete Workout!", "alert-danger")
    
    return redirect("main:home_view")


def new_set_view(request:HttpRequest, workout_id:int):
    
    if request.method == "POST":
        workout = Workout.objects.get(pk=workout_id)
                
        if request.POST['repetition'].isdigit():
            weight = request.POST["weight"]
            try:
                weight = float(weight) 
                if weight <= 0:
                    messages.error(request, "Weight must be a positive number.", "alert-danger")
                else:
                    new_set = Set(weight=weight, repetition=int(request.POST['repetition']), workout=workout)
                    new_set.save()
                    messages.success(request, "Added Set Successfuly!", "alert-success")
                    return redirect("routines:routine_detail_view", routine_id=workout.routine.id)
            except ValueError:
                messages.error(request, "Weight must be a valid number.", "alert-danger")
        else:
            messages.error(request, "Couldn't Add Set! Please correct the errors.", "alert-danger")
            
    else:
        messages.error(request, "Couldn't Add Set!. Please correct the errors.", "alert-danger")
    
    return render(request, "sets/new_set.html")


def update_set_view(request:HttpRequest, workout_id:int, set_id:int):
    set = Set.objects.get(pk=set_id)
    
    # if request.method == "POST":
    #     set_form = SetForm(instance=set, data=request.POST)
    #     if set_form.is_valid():
    #         set_form.save()
    #         messages.success(request, "Updated Set Successfuly!", "alert-success")
    #         return redirect("main:home_view")
    #     else:
    #         print("not valid form", set_form.errors)
    #         messages.error(request, "Couldn't Update Set!", "alert-danger")
    
    return render(request, "sets/update_set.html")

def delete_set_view(request:HttpRequest, workout_id:int, set_id:int):
    try:
        set = Set.objects.get(pk=set_id)
        set.delete()
        messages.success(request, "Deleted Set Successfuly!", "alert-success")
    except Exception as e:
        print(e)
        messages.error(request, "Couldn't Delete Set!", "alert-danger")
    
    return redirect("main:home_view")



def search_workouts_view(request:HttpRequest):
    if "search" in request.GET and len(request.GET["search"]) >= 3:
        workouts = Workout.objects.filter(name__contains=request.GET["search"])
    
    else:
        messages.error(request, "Couldn't Find Workout!", "alert-danger")
        workouts = []
    
    return render(request, "workouts/search_workout.html", {'workouts': workouts,})

    
    
    


    
    
    
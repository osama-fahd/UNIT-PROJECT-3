from django import forms
from .models import Workout, Set


class WorkoutForm(forms.ModelForm):
    class Meta:
        model = Workout
        fields = "__all__"
        
        
class SetForm(forms.ModelForm):
    class Meta:
        model = Set
        fields = "__all__"
from django.shortcuts import render
from .models import Habit
from django.contrib.auth.decorators import login_required

@login_required
def habit_list(request):
    habits = Habit.objects.filter(user=request.user)
    return render(request, 'habits/habit_list.html', {'habits': habits})

from django.shortcuts import render

def habit_list(request):
    return render(request, 'habits/habit_list.html')

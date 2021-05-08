from django.shortcuts import render

# Create your views here.

def enter_list(request):
    return render(request, "enter.html", {})
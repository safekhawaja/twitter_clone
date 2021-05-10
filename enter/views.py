from django.shortcuts import render
from django.contrib.auth import authenticate, login
from enter.models import User

def enter_list(request):
    users = User.name.all() # query set
    return render(request, "enter.html", {'user': users})


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("/")
    return render(request, 'accounts.html', {})


def logout_(request):
    logout(request)
    return redirect("/login")


def signup_view(request):
	user = User.objects.create_user(username=request.POST['username'],
					email=request.POST['email'],
					password=request.POST['password'])
	login(request, user)
	return redirect('/')
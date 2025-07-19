from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

# Create your views here.
def index(request):
    return render(request, "index.html")
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, "about.html")
    

def social_events(request):
    return render(request, "social_events.html")

def corporate_events(request):
    return render(request, "corporate_events.html")

def seasonal_events(request):
    return render(request, "seasonal_events.html")

def entertainment_events(request):
    return render(request, "entertainment_events.html")

def health_events(request):
    return render(request, "health_events.html")

def educational_events(request):
    return render(request, "educational_events.html")

def contact(request):
    return render(request, "contact.html")
    #return HttpResponse("this is contactpage")




def register_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        # Validate fields
        if password != confirm_password:
            messages.error(request, "Passwords do not match.")
        elif User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists.")
        elif User.objects.filter(email=email).exists():
            messages.error(request, "Email already registered.")
        else:
            # Create and save the user
            user = User.objects.create_user(username=username, email=email, password=password)
            user.save()
            messages.success(request, "Registration successful. Please log in.")
            return redirect('/login')

    return render(request, 'register.html')
from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.core.mail import send_mail


from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required



from .form import SocialEventForm
from .form import SeasonalEventForm
from .form import HealthEventForm
from .form import EntertainmentEventForm
from .form import CorporateEventForm
from .form import EducationalEventForm
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import DandiyaBooking


# Create your views here.
def index(request):
    return render(request, "index.html")
    #return HttpResponse("this is homepage")

def about(request):
    return render(request, "about.html")
    

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

def membership(request):
    return render(request, "membership.html")
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




















# MEMBERSHIP PAGE
def membership(request):
    return render(request, 'membership.html')


# MEMBERSHIP REQUEST FORM (sends email)
def membership_request(request):
    if request.method == 'POST' and 'verify_id' in request.POST:
        id_no = request.POST.get('id_no')
        id_type = request.POST.get('id_type')
        image = request.FILES.get('image')

        send_mail(
            subject='ID Verification Request',
            message=f"ID No: {id_no}\nID Type: {id_type}\nA new ID verification request has been submitted.",
            from_email=settings.DEFAULT_FROM_EMAIL,
            recipient_list=[settings.ADMIN_EMAIL],
        )
        return render(request, 'thankyou.html')

    return render(request, 'membership.html')






@login_required
def social_events(request):
    if request.method == 'POST':
        form = SocialEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user  # Link with logged-in user
            event.save()
            return redirect('index')  # or any thank you page
    else:
        form = SocialEventForm()

    return render(request, 'social_events.html', {
        'form': form,
        'username': request.user.username
    })

@login_required
def seasonal_events(request):
    if request.method == 'POST':
        form = SeasonalEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('seasonal_events')  # You can redirect to a "thank you" page instead
    else:
        form = SeasonalEventForm()

    return render(request, 'seasonal_events.html', {
        'form': form,
        'username': request.user.username
    })

@login_required
def health_events(request):
    if request.method == 'POST':
        form = HealthEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('health_events.html')  # You can redirect to a "thank you" page instead
    else:
        form = HealthEventForm()

    return render(request, 'health_events.html', {
        'form': form,
        'username': request.user.username
    })

@login_required
def entertainment_events(request):
    if request.method == 'POST':
        form = EntertainmentEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('entertainment_events.html')  # You can redirect to a "thank you" page instead
    else:
        form = EntertainmentEventForm()

    return render(request, 'entertainment_events.html', {
        'form': form,
        'username': request.user.username
    })
@login_required
def corporate_events(request):
    if request.method == 'POST':
        form = CorporateEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('corporate_events.html')  # You can redirect to a "thank you" page instead
    else:
        form = CorporateEventForm()

    return render(request, 'corporate_events.html', {
        'form': form,
        'username': request.user.username
    })
@login_required
def educational_events(request):
    if request.method == 'POST':
        form = EducationalEventForm(request.POST)
        if form.is_valid():
            event = form.save(commit=False)
            event.user = request.user
            event.save()
            return redirect('educational_events.html')  # You can redirect to a "thank you" page instead
    else:
        form = EducationalEventForm()

    return render(request, 'educational_events.html', {
        'form': form,
        'username': request.user.username
    })


# TESTING TEXT RESPONSE
def get_response(request):
    return HttpResponse("This is the get_response view.")
def DandiyaBooking(request):
    return render(request, "dandiya.html")
@csrf_exempt
def save_booking(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        datetime = data.get('datetime')

        DandiyaBooking.objects.create( datetime=datetime)

        return JsonResponse({'status': 'success'})
    return JsonResponse({'status': 'error'}, status=400)



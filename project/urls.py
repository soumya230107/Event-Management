from django.contrib import admin
from django.urls import path
from project import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path("", views.index, name="project"),
    path("about", views.about, name="about"),
    path("contact", views.contact, name="contact"),
    path("social-events/", views.social_events, name="social_events"),
    path("corporate-events/", views.corporate_events, name="corporate_events"),
    path("seasonal-events/", views.seasonal_events, name="seasonal_events"),
    path("entertainment-events/", views.entertainment_events, name="entertainment_events"),
    path("health-events/", views.health_events, name="health_events"),
    path("educational-events/", views.educational_events, name="educational_events"),


    path("register/", views.register_view, name="register"),
    path("login/", auth_views.LoginView.as_view(template_name='login.html'), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),


    
]



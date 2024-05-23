from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.landing_page, name='landing-page'),
	path('contact', views.contact_us, name='contact-page'),
	path('about', views.about_us, name='about-page'),
] 
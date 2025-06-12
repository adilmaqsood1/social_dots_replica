from django.shortcuts import render
from .models import (
    SiteSettings, NavItem, Hero, ServiceCategory, 
    Client, Testimonial
)

# Create your views here.
def home(request):
    context = {
        'site_settings': SiteSettings.objects.first(),
        'nav_items': NavItem.objects.all(),
        'hero': Hero.objects.first(),
        'service_categories': ServiceCategory.objects.all(),
        'clients': Client.objects.all(),
        'testimonials': Testimonial.objects.all(),
    }
    return render(request, 'core/home.html', context)

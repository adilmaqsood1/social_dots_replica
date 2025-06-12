from django.contrib import admin
from .models import (
    SiteSettings, NavItem, Hero, HeroImage, 
    ServiceCategory, ServiceFeature, Client, Testimonial
)

# Register your models here.
@admin.register(SiteSettings)
class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ('site_name',)

@admin.register(NavItem)
class NavItemAdmin(admin.ModelAdmin):
    list_display = ('title', 'url', 'order')
    list_editable = ('order',)

class HeroImageInline(admin.TabularInline):
    model = HeroImage
    extra = 1

@admin.register(Hero)
class HeroAdmin(admin.ModelAdmin):
    list_display = ('heading_first_part', 'heading_second_part', 'heading_third_part')
    inlines = [HeroImageInline]

class ServiceFeatureInline(admin.TabularInline):
    model = ServiceFeature
    extra = 3

@admin.register(ServiceCategory)
class ServiceCategoryAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)
    inlines = [ServiceFeatureInline]

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ('name', 'order')
    list_editable = ('order',)

@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_title', 'order')
    list_editable = ('order',)

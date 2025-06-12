from django.db import models

# Create your models here.
class SiteSettings(models.Model):
    logo = models.ImageField(upload_to='logos/')
    site_name = models.CharField(max_length=100, default='Social Dots')
    
    def __str__(self):
        return self.site_name
    
    class Meta:
        verbose_name_plural = "Site Settings"

class NavItem(models.Model):
    title = models.CharField(max_length=50)
    url = models.CharField(max_length=100)
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        ordering = ['order']

class Hero(models.Model):
    heading_first_part = models.CharField(max_length=100, default='Empowering')
    heading_second_part = models.CharField(max_length=100, default='Canadian Businesses')
    heading_third_part = models.CharField(max_length=100, default='with Digital solutions.')
    cta_text = models.CharField(max_length=50, default='Start Your Project')
    cta_url = models.CharField(max_length=100, default='#')
    
    def __str__(self):
        return f"{self.heading_first_part} {self.heading_second_part}"
    
    class Meta:
        verbose_name_plural = "Hero Section"

class HeroImage(models.Model):
    hero = models.ForeignKey(Hero, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to='hero/')
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"Hero Image {self.order}"
    
    class Meta:
        ordering = ['order']

class ServiceCategory(models.Model):
    title = models.CharField(max_length=100)
    icon = models.CharField(max_length=100, help_text="Icon class or code")
    description = models.TextField()
    image = models.ImageField(upload_to='services/')
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = "Service Categories"
        ordering = ['order']

class ServiceFeature(models.Model):
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE, related_name='features')
    title = models.CharField(max_length=100)
    
    def __str__(self):
        return f"{self.category.title} - {self.title}"

class Client(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='clients/')
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        ordering = ['order']

class Testimonial(models.Model):
    client_name = models.CharField(max_length=100)
    client_title = models.CharField(max_length=100)
    content = models.TextField()
    order = models.IntegerField(default=0)
    
    def __str__(self):
        return f"{self.client_name} - {self.client_title}"
    
    class Meta:
        ordering = ['order']

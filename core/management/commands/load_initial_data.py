from django.core.management.base import BaseCommand
from core.models import (
    SiteSettings, NavItem, Hero, HeroImage, 
    ServiceCategory, ServiceFeature, Client, Testimonial
)
from django.core.files.images import ImageFile
import os

class Command(BaseCommand):
    help = 'Load initial data for the Social Dots website'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting to load initial data...'))
        
        # Create site settings
        site_settings, created = SiteSettings.objects.get_or_create(
            site_name='Social Dots'
        )
        self.stdout.write(self.style.SUCCESS(f'Site settings {"created" if created else "updated"}'))
        
        # Create navigation items
        nav_items = [
            {'title': 'Home', 'url': '/', 'order': 1},
            {'title': 'Services', 'url': '#services', 'order': 2},
            {'title': 'Portfolio', 'url': '#portfolio', 'order': 3},
            {'title': 'About', 'url': '#about', 'order': 4},
        ]
        
        for item in nav_items:
            NavItem.objects.get_or_create(
                title=item['title'],
                defaults={'url': item['url'], 'order': item['order']}
            )
        self.stdout.write(self.style.SUCCESS('Navigation items created'))
        
        # Create hero section
        hero, created = Hero.objects.get_or_create(
            heading_first_part='Empowering',
            heading_second_part='Canadian Businesses',
            heading_third_part='with Digital solutions.',
            cta_text='Start Your Project',
            cta_url='#contact'
        )
        self.stdout.write(self.style.SUCCESS(f'Hero section {"created" if created else "updated"}'))
        
        # Create service categories with features
        services = [
            {
                'title': 'Web Development',
                'icon': 'fas fa-code',
                'description': 'Modern, scalable websites and web apps.',
                'features': [
                    'Custom Website Development',
                    'eCommerce Solutions',
                    'API Integrations',
                    'Performance Optimization'
                ]
            },
            {
                'title': 'UI/UX Design',
                'icon': 'fas fa-paint-brush',
                'description': 'Intuitive and engaging user interfaces.',
                'features': [
                    'User Research & Personas',
                    'Wireframing & Prototyping',
                    'Visual Design Systems',
                    'Usability Testing'
                ]
            },
            {
                'title': 'AI Agents & Automation Tools',
                'icon': 'fas fa-robot',
                'description': 'Advanced AI Agents and automation tools to help your business grow, support customers 24/7, and automate workflows.',
                'features': [
                    'Custom AI Agents for Websites',
                    'Automated Customer Support with AI Agents',
                    'Lead Generation AI Agents',
                    'Integration with CRM & Messaging Platforms using AI Agents'
                ]
            },
            {
                'title': 'Digital Marketing',
                'icon': 'fas fa-chart-line',
                'description': 'Data-driven digital marketing strategies that deliver measurable results.',
                'features': [
                    'Comprehensive Digital Strategy',
                    'Search Engine Marketing (SEM)',
                    'Social Media Marketing',
                    'Content Marketing'
                ]
            },
            {
                'title': 'Content Creation',
                'icon': 'fas fa-pen',
                'description': 'Impactful content that tells your story and drives engagement.',
                'features': [
                    'Copywriting & Blogging',
                    'Video Production',
                    'Graphic Design',
                    'Brand Storytelling'
                ]
            },
            {
                'title': 'Salesforce Implementation',
                'icon': 'fas fa-cloud',
                'description': 'Expert Salesforce solutions: consulting, implementation, integration, and support.',
                'features': [
                    'Salesforce Consulting',
                    'Implementation & Data Migration',
                    'Custom Development & Automation',
                    'Integration with Third-Party Tools',
                    'Ongoing Support & Optimization',
                    'Analytics & Reporting'
                ]
            }
        ]
        
        for i, service in enumerate(services):
            category, created = ServiceCategory.objects.get_or_create(
                title=service['title'],
                defaults={
                    'icon': service['icon'],
                    'description': service['description'],
                    'order': i
                }
            )
            
            for feature in service['features']:
                ServiceFeature.objects.get_or_create(
                    category=category,
                    title=feature
                )
        
        self.stdout.write(self.style.SUCCESS('Service categories and features created'))
        
        # Create testimonials
        testimonials = [
            {
                'client_name': 'Saahil',
                'client_title': 'Social Media Content Creator',
                'content': 'As a new Content Creator, I was overwhelmed with making videos and the production. I tried many apps but it was slowing me down. Ali made things simple and affordable. I finally felt confident putting my brand online at the speed I wanted.',
                'order': 1
            },
            {
                'client_name': 'Mahi',
                'client_title': 'Etsy Creator',
                'content': 'I run a small Etsy shop and needed help setting up a simple landing page. I expected tech jargon and delays—but got the exact opposite. Ali explained everything in plain language and delivered faster than I thought possible.',
                'order': 2
            },
            {
                'client_name': 'Pankaj',
                'client_title': 'Home Run Business',
                'content': 'I never felt like a \'small client.\' I needed help with just a few video edits and captions, but Ali treated it like a real project—with timelines, feedback, and care. That level of respect meant a lot to me.',
                'order': 3
            },
            {
                'client_name': 'Mike',
                'client_title': 'Local Business Owner',
                'content': 'I didn\'t need a full agency—I just needed someone to guide me through setting up my Google Business profile and improving my local SEO. Ali\'s advice was spot-on, actionable, and helped bring in real leads.',
                'order': 4
            }
        ]
        
        for testimonial in testimonials:
            Testimonial.objects.get_or_create(
                client_name=testimonial['client_name'],
                client_title=testimonial['client_title'],
                defaults={
                    'content': testimonial['content'],
                    'order': testimonial['order']
                }
            )
        
        self.stdout.write(self.style.SUCCESS('Testimonials created'))
        
        self.stdout.write(self.style.SUCCESS('All initial data loaded successfully!'))
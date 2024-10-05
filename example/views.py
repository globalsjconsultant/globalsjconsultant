from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from datetime import datetime

from django.http import HttpResponse

def index(request):
    now = datetime.now()
    html = f'''
    <html>
        <body>
            <h1>Hello from Vercel! nothing changed</h1>
            <p>The current time is { now }.</p> wah yar
        </body>
    </html>
    '''
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')
def team(request):
    return render(request, 'team.html')
def team_detail(request):
    return render(request, 'team_detail.html')
def notfound(request):
    return render(request, 'notfound.html')
def faq(request):
    return render(request, 'faq.html')
def service(request):
    return render(request, 'service.html')
def service_detail(request):
    return render(request, 'service_detail.html')

def coaching(request):
    return render(request, 'coaching.html')
def coaching_detail(request):
    return render(request, 'coaching_detail.html')
def country(request):
    return render(request, 'country.html')
def country_detail(request):
    return render(request, 'country_detail.html')

def blog(request):
    return render(request, 'blog.html')
def blog_detail(request):
    return render(request, 'blog_detail.html')

def contact(request):
    return render(request, 'contact.html')

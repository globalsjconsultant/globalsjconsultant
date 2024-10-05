from django.urls import path
from . import views

app_name = 'example'

urlpatterns = [
    path('', views.index, name='index'),
    path('about', views.about, name='about'),

    path('team', views.team, name='team'),
    path('team_detail', views.team_detail, name='team_detail'),

    path('service', views.service, name='service'),
    path('service_detail', views.service_detail, name='service_detail'),

    path('blog', views.blog, name='blog'),
    path('blog_detail', views.blog_detail, name='blog_detail'),


    path('coaching', views.coaching, name='coaching'),
    path('coaching_detail', views.coaching_detail, name='coaching_detail'),

    path('country', views.country, name='country'),
    path('country_detail', views.country_detail, name='country_detail'),

    path('404', views.notfound, name='404'),
    path('faq', views.faq, name='faq'),
    path('service', views.service, name='service'),
    path('contact', views.contact, name='contact')

]
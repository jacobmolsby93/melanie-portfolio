from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio2/', views.paint_portfolio, name='portfolio2'),
    path('about/', views.about, name='about')
]
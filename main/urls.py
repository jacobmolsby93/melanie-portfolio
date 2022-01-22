from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('add_image/', views.add_image, name='add_image'),
    path('add_painting/', views.add_painting, name='add_painting'),
    path('image/<int:image_id>/', views.delete_image, name="delete_image"),
    path('painting/<int:painting_id>/', views.delete_painting, name="delete_painting"),
    path('edit_image/<int:image_id>/', views.edit_image, name="edit_image"),
    path('edit_painting/<int:painting_id>/', views.edit_painting, name="edit_painting"),
    path('portfolio/<int:page>/', views.portfolio, name='portfolio'),
    path('portfolio2/', views.paint_portfolio, name='portfolio2'),
    path('site_management/', views.site_management, name='site_management')
]
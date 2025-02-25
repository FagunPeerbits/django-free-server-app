from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('upload/', views.image_upload, name='image-upload'),
    path('images/', views.get_images, name='get-images')
]

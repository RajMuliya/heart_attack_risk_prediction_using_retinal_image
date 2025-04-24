from django.urls import path
from . import views

urlpatterns = [
    path('', views.upload_image, name='upload_image'),
    path('how-it-works/', views.hitw, name='how-it-works'),
    path('about/', views.aboutpage, name='about'),
    path('faq/', views.faqpage, name='faq'),
]
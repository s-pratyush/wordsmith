from django.urls import path
from django.views.generic import TemplateView

from . import views
app_name = 'wordsmith'
urlpatterns = [
    path('', views.index, name='index'),
    path('form/',views.form,name='form'),
]

from django.urls import path
from django.views.generic import TemplateView

from . import views
app_name = 'wordsmith'
urlpatterns = [
    path('', views.index, name='index'),
    path('cv_form/',views.cv_design,name='cv_design'),
    path('form/',views.form,name='form'),
]

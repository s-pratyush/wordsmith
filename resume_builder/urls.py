from django.urls import path
from django.conf.urls import url
from django.views.generic import TemplateView

from . import views
from .views import logout


app_name = 'resume_builder'
urlpatterns = [
    path('', views.index, name='index'),
    path('cv_form/',views.cv_design,name='cv_design'),
    path('form/',views.form,name='form'),
    url('resume/',views.resume,name='resume'),
    path('signup/',views.signup,name='signup'),
    path('login/',views.log_in,name='login'),
]

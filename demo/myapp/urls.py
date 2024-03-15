from django.urls import path
from . import views
from .views import  process_form, patient_list, medical_records_list, prediction_results_list


urlpatterns = [
    path('accounts/login/', views.login_view, name='login'),
    path('accounts/logout/', views.logout_view, name='logout'),
    path("", views.process_form, name="process_form"),
    path('patients/', patient_list, name='patient_list'),
    path('medical_records/', medical_records_list, name='medical_records_list'),
    path('prediction_results/', views.prediction_results_list, name='prediction_results_list'),
    path('about/', views.about_page, name='about'),
    path('technical-support/', views.technical_support, name='technical_support')
]
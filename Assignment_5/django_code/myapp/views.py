from django.shortcuts import render, HttpResponse, redirect, get_object_or_404,reverse
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import  MedicalRecords,PredictionResults, Patients
from .forms import  MedicalRecordsForm

import joblib
import numpy as np
model = joblib.load('model/model_heart.pkl')



def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('process_form') 
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('login') 

@login_required
def home(request):
    return render(request, "home.html")

def process_form(request):
    if request.method == 'POST':
        form = MedicalRecordsForm(request.POST)
        if form.is_valid():
            medical_record = form.save()

            data_for_prediction = preprocess_data(medical_record)
            print(data_for_prediction)

            prediction = model.predict(np.array(list(data_for_prediction.values())).reshape(1, -1))
            print(prediction)
            
            if prediction == 1:
                print('Heart ❤️ disease - Unlikely')
                prediction_risk = 'no risk'
            else:
                print('Heart 💔 disease - Likely.')
                prediction_risk = 'risk'
            
            risk_prob = model.predict_proba(np.array(list(data_for_prediction.values())).reshape(1, -1))[0][1]

            save_prediction_result(medical_record, prediction_risk,risk_prob)

            prediction_list = prediction.tolist()

            return JsonResponse({'prediction': prediction_list})
    else:
        form = MedicalRecordsForm()

    return render(request, 'heart_status.html', {'form': form})

# preprocessing data 
def preprocess_data(medical_record):
    data_for_prediction = {
        'age': medical_record.age,
        'sex': medical_record.sex,
        'chest_pain': medical_record.chest_pain,
        'blood_pressure': medical_record.blood_pressure,
        'fasting_bs' : medical_record.fasting_bs,
        'resting_ecg' : medical_record.resting_ecg,
        'exercise_angina' : medical_record.exercise_angina,
        'cholesterol' : medical_record.cholesterol,
        'heart_rate' : medical_record.heart_rate,
        'st_depression' : medical_record.st_depression,
        'slope' : medical_record.slope,
        'vessels' : medical_record.vessels,
        'thal' : medical_record.thal
        }
    return data_for_prediction

def save_prediction_result(medical_record, prediction,risk_probability):
    PredictionResults.objects.create(
        record_id=medical_record,
        prediction_result=prediction,
        risk_probability=risk_probability
    )

def patient_list(request):
    patients = Patients.objects.all()
    return render(request, 'patient_list.html', {'patients': patients})

def medical_records_list(request):
    medical_records = MedicalRecords.objects.all()
    return render(request, 'medical_records_list.html', {'medical_records': medical_records})


def prediction_results_list(request):
    prediction_results = PredictionResults.objects.all()
    return render(request, 'prediction_results_list.html', {'prediction_results': prediction_results})

def about_page(request):
    return render(request, 'about.html')

def technical_support(request):
    return render(request, 'technical_support.html')
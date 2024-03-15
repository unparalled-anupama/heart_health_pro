from django import forms
from .models import  MedicalRecords
from django.core.validators import MinValueValidator, MaxValueValidator

# class HeartDisease(forms.ModelForm):


# Medical Records form
class MedicalRecordsForm(forms.ModelForm):
    class Meta:
        model = MedicalRecords
        fields = [
            'date', 'patient_id', 'age', 'sex', 'chest_pain', 'blood_pressure', 'fasting_bs',
            'resting_ecg', 'exercise_angina', 'cholesterol', 'heart_rate', 'st_depression',
            'slope', 'vessels', 'thal', 'remarks']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'patient_id': forms.Select(attrs={'class': 'form-control'}),
            'age': forms.NumberInput(attrs={'class': 'form-control', 'min': '20', 'max': '80'}),
            'sex': forms.Select(attrs={'class': 'form-select'}),
            'chest_pain': forms.Select(attrs={'class': 'form-select'}),
            'blood_pressure': forms.NumberInput(attrs={'class': 'form-control', 'min': '90', 'max': '200'}),
            'fasting_bs': forms.Select(attrs={'class': 'form-select'}),
            'resting_ecg': forms.Select(attrs={'class': 'form-select'}),
            'exercise_angina': forms.Select(attrs={'class': 'form-select'}),
            'cholesterol': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '500'}),
            'heart_rate': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '300'}),
            'st_depression': forms.NumberInput(attrs={'class': 'form-control', 'min': '0', 'max': '10'}),
            'slope': forms.Select(attrs={'class': 'form-select'}),
            'vessels': forms.Select(attrs={'class': 'form-select'}),
            'thal': forms.Select(attrs={'class': 'form-select'}),
            'remarks': forms.Textarea(attrs={'class': 'form-control', 'rows': '3'}),
        }

        labels = {
            'date': 'Date of Test',
            'patient_id': 'Patient ID',
            'age': 'Age',
            'sex': 'Sex',
            'chest_pain': 'Chest pain type',
            'blood_pressure': 'Resting blood pressure',
            'fasting_bs': 'Fasting blood sugar',
            'resting_ecg': 'Resting electrocardiographic results',
            'exercise_angina': 'Exercise induced angina',
            'cholesterol': 'Serum cholesterol',
            'heart_rate': 'Maximum heart rate achieved',
            'st_depression': 'ST depression induced by exercise relative to rest',
            'slope': 'Slope of the peak exercise ST segment',
            'vessels': 'Number of major vessels colored by flourosopy',
            'thal': 'Thalassemia',
            'remarks': 'Remarks',
        }
    



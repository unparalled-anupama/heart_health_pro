from django.contrib import admin
from .models import Patients, MedicalRecords, PredictionResults

# Register your models here.
admin.site.register(Patients)
admin.site.register(MedicalRecords)
admin.site.register(PredictionResults)
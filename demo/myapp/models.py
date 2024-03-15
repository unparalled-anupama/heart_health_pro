from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Model for the Patient's personal info
class Patients(models.Model):
    patient_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length= 20)
    last_name = models.CharField(max_length=20)
    date_of_birth = models.DateField()
    sex = models.CharField(max_length=10)
    height = models.FloatField()
    weight = models.FloatField()
    blood_type = models.CharField(max_length=5)
    city = models.CharField(max_length=100)
    street = models.CharField(max_length=100)
    telephone_number = models.CharField(max_length=15)
    insurance_number = models.CharField(max_length=50)


# Model for the Records of the test which will be used for the prediction
class MedicalRecords(models.Model):

    SEX_CHOICES = [(0, 'Male'), (1, 'Female')]
    CP_CHOICES = [
        (0, 'Typical Angina'),
        (1, 'Atypical Angina'),
        (2, 'Non-anginal Pain'),
        (3, 'Asymptomatic')
    ]
    FASTING_CHOICES = [(0, 'False'), (1, 'True')]
    RESTECG_CHOICES = [
        (0, 'Normal'),
        (1, 'Having ST-T wave abnormality'),
        (2, 'Probable or definite left ventricular hypertrophy')
    ]
    EXE_ANGINA_CHOICES = [(0, 'No'), (1, 'Yes')]
    SLOPE_CHOICES = [(0, 'Upsloping'), (1, 'Flat'), (2, 'Downsloping')]
    VESSELS_CHOICES = [(i, str(i)) for i in range(4)]
    THAL_CHOICES = [(3, 'Normal'), (6, 'Fixed defect'), (7, 'Reversible defect')]

    date = models.DateField()
    record_id = models.AutoField(primary_key=True)
    patient_id = models.ForeignKey('Patients', on_delete=models.CASCADE)
    age = models.IntegerField(validators=[MinValueValidator(20), MaxValueValidator(80)])
    sex = models.IntegerField(choices=SEX_CHOICES)
    chest_pain = models.IntegerField(choices=CP_CHOICES)
    blood_pressure = models.IntegerField(validators=[MinValueValidator(90), MaxValueValidator(200)])
    fasting_bs = models.IntegerField(choices=FASTING_CHOICES)
    resting_ecg= models.IntegerField(choices=RESTECG_CHOICES)
    exercise_angina = models.IntegerField(choices=EXE_ANGINA_CHOICES)
    cholesterol = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(500)])
    heart_rate = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(300)])
    st_depression = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    slope = models.IntegerField(choices=SLOPE_CHOICES)
    vessels = models.IntegerField(choices= VESSELS_CHOICES)
    thal = models.IntegerField(choices=THAL_CHOICES)
    remarks = models.TextField(blank=True, null=True)


# Model for the prediction of the Medical Records
class PredictionResults(models.Model):
    prediction_id = models.AutoField(primary_key=True)
    record_id = models.ForeignKey('MedicalRecords', on_delete=models.CASCADE)
    prediction_result = models.CharField(max_length=10)
    risk_probability = models.FloatField(default=0.0)
# Generated by Django 5.0.3 on 2024-03-09 16:45

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Patients',
            fields=[
                ('patient_id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=20)),
                ('last_name', models.CharField(max_length=20)),
                ('date_of_birth', models.DateField()),
                ('sex', models.CharField(max_length=10)),
                ('height', models.FloatField()),
                ('weight', models.FloatField()),
                ('blood_type', models.CharField(max_length=5)),
                ('city', models.CharField(max_length=100)),
                ('street', models.CharField(max_length=100)),
                ('telephone_number', models.CharField(max_length=15)),
                ('insurance_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='MedicalRecords',
            fields=[
                ('date', models.DateField()),
                ('record_id', models.AutoField(primary_key=True, serialize=False)),
                ('age', models.IntegerField(validators=[django.core.validators.MinValueValidator(20), django.core.validators.MaxValueValidator(80)])),
                ('sex', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default='male', max_length=10)),
                ('chest_pain', models.CharField(choices=[('Typical angina', 'Typical Angina'), ('Atypical angina', 'Atypical Angina'), ('Non-anginal pain', 'Non Anginal Pain'), ('Asymptomatic', 'Asymptomatic')], default='Typical angina', max_length=20)),
                ('blood_pressure', models.IntegerField(validators=[django.core.validators.MinValueValidator(90), django.core.validators.MaxValueValidator(200)])),
                ('fasting_bs', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=20)),
                ('resting_ecg', models.CharField(choices=[('Normal', 'Normal'), ('ST-T wave abnormality', 'St T Wave Abnormality'), ('Probable or left ventricular hypertrophy', 'Probable Or  Left Ventricular Hypertrophy')], default='Normal', max_length=50)),
                ('exercise_angina', models.CharField(choices=[('Yes', 'Yes'), ('No', 'No')], default='Yes', max_length=20)),
                ('cholesterol', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(500)])),
                ('heart_rate', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(300)])),
                ('st_depression', models.FloatField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('slope', models.CharField(choices=[('Unsloping', 'Unsloping'), ('Flat', 'Flat'), ('Downsloping', 'Downsloping')], default='Unsloping', max_length=20)),
                ('vessels', models.IntegerField(choices=[(0, 'Zero'), (1, 'One'), (2, 'Two'), (3, 'Three')], default=0)),
                ('thal', models.CharField(choices=[('Normal', 'Normal'), ('Fixed Defect', 'Fixed Defect'), ('Reversible_Defect', 'Reversible Defect')], default='Normal', max_length=20)),
                ('remarks', models.TextField(blank=True, null=True)),
                ('patient_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.patients')),
            ],
        ),
        migrations.CreateModel(
            name='PredictionResults',
            fields=[
                ('prediction_id', models.AutoField(primary_key=True, serialize=False)),
                ('prediction_result', models.CharField(max_length=3)),
                ('prediction_datetime', models.DateTimeField()),
                ('record_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.medicalrecords')),
            ],
        ),
    ]

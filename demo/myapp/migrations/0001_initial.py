# Generated by Django 5.0.3 on 2024-03-09 15:47

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HeartDisease',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('patient_id', models.CharField(max_length=100)),
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
            ],
        ),
        migrations.CreateModel(
            name='MyModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('message', models.CharField(choices=[('male', 'Male'), ('female', 'Female'), ('others', 'Others')], default='male', max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='TodoItem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('completed', models.BooleanField(default=False)),
            ],
        ),
    ]

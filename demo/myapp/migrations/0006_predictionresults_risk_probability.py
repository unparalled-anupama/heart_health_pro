# Generated by Django 5.0.3 on 2024-03-10 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_remove_predictionresults_prediction_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='predictionresults',
            name='risk_probability',
            field=models.FloatField(default=0.0),
        ),
    ]

# Generated by Django 5.0.3 on 2024-03-09 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_alter_medicalrecords_chest_pain_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicalrecords',
            name='vessels',
            field=models.IntegerField(choices=[(0, '0'), (1, '1'), (2, '2'), (3, '3')]),
        ),
    ]
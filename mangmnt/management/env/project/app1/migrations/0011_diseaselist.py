# Generated by Django 4.1.5 on 2023-01-25 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0010_alter_patient_disease_alter_patient_doctorname'),
    ]

    operations = [
        migrations.CreateModel(
            name='DiseaseList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('diseasename', models.CharField(max_length=150)),
                ('symptoms', models.CharField(max_length=150)),
                ('doctorname', models.CharField(max_length=150)),
            ],
        ),
    ]
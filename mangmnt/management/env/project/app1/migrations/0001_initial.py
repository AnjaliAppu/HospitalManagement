# Generated by Django 4.1.5 on 2023-01-17 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patientname', models.CharField(max_length=150)),
                ('address', models.TextField()),
                ('age', models.CharField(max_length=100)),
                ('gender', models.CharField(max_length=100)),
                ('contactnum', models.CharField(max_length=100)),
                ('disease', models.CharField(max_length=150)),
                ('doctorname', models.CharField(max_length=100)),
            ],
        ),
    ]

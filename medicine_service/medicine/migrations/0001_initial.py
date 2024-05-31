# Generated by Django 3.0.5 on 2024-05-31 01:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PatientMedicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.IntegerField()),
            ],
            options={
                'verbose_name': 'patient_medicine',
            },
        ),
        migrations.CreateModel(
            name='Producer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('email', models.CharField(max_length=100)),
            ],
            options={
                'verbose_name': 'Producer',
            },
        ),
        migrations.CreateModel(
            name='Medicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('sl', models.IntegerField()),
                ('note', models.CharField(max_length=255)),
                ('gia', models.CharField(max_length=255)),
                ('producer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.Producer')),
            ],
            options={
                'verbose_name': 'Medicine',
            },
        ),
        migrations.CreateModel(
            name='ItemPatientMedicine',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sl', models.IntegerField()),
                ('note', models.CharField(max_length=255)),
                ('medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.Medicine')),
                ('patient_medicine', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='medicine.PatientMedicine')),
            ],
            options={
                'verbose_name': 'item_patient_medicine',
            },
        ),
    ]

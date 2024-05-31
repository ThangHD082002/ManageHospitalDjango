# Generated by Django 3.0.5 on 2024-05-31 02:23

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Examination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('timeStart', models.DateTimeField(default=django.utils.timezone.now)),
                ('price', models.FloatField()),
                ('doctor', models.IntegerField()),
            ],
            options={
                'verbose_name': 'examination',
            },
        ),
        migrations.CreateModel(
            name='PatientExamination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('patient', models.IntegerField()),
            ],
            options={
                'verbose_name': 'patient_examination',
            },
        ),
        migrations.CreateModel(
            name='ItemPatientExamination',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=255)),
                ('examination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.Examination')),
                ('patient_examination', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='examination.PatientExamination')),
            ],
            options={
                'verbose_name': 'item_patient_examination',
            },
        ),
    ]

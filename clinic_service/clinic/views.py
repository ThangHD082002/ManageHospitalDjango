
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import TypeClinic, Clinic, Bed
from .serializers import TypeClinicSerializer, ClinicSerializer, BedSerializer, ClinicSerializer1, BedSerializer1

@api_view(['POST'])
def add_type_clinic(request):
    serializer = TypeClinicSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_clinic(request):
    serializer = ClinicSerializer1(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def add_bed(request):
    serializer = BedSerializer1(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def get_bed_by_clinic_id(request, clinic_id):
    beds = Bed.objects.filter(clinic_id=clinic_id)
    serializer = BedSerializer(beds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_bed_by_id(request, id):
    bed = get_object_or_404(Bed, id=id)
    serializer = BedSerializer(bed)
    return Response(serializer.data)

@api_view(['GET'])
def get_clinic_by_typeclinic_id(request, type_clinic_id):
    clinics = Clinic.objects.filter(type_clinic_id=type_clinic_id)
    serializer = ClinicSerializer(clinics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_clinic_by_id(request, id):
    clinic = get_object_or_404(Clinic, id=id)
    serializer = ClinicSerializer(clinic)
    return Response(serializer.data)


@api_view(['GET'])
def get_type_clinic_by_id(request, id):
    clinic = get_object_or_404(TypeClinic, id=id)
    serializer = TypeClinicSerializer(clinic)
    return Response(serializer.data)




@api_view(['GET'])
def get_all_type_clinics(request):
    type_clinics = TypeClinic.objects.all()
    serializer = TypeClinicSerializer(type_clinics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_clinics(request):
    clinics = Clinic.objects.all()
    serializer = ClinicSerializer(clinics, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_all_beds(request):
    beds = Bed.objects.all()
    serializer = BedSerializer(beds, many=True)
    return Response(serializer.data)
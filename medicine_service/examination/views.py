from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Examination, PatientExamination, ItemPatientExamination
from .serializers import ExaminationSerializer, PatientExaminationSerializer, ItemPatientExaminationSerializer, ItemPatientExaminationSerializer1

# POST add Examination
@api_view(['POST'])
def add_examination(request):
    serializer = ExaminationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST add PatientExamination
@api_view(['POST'])
def add_patient_examination(request):
    serializer = PatientExaminationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST add ItemPatientExamination
@api_view(['POST'])
def add_item_patient_examination(request):
    serializer = ItemPatientExaminationSerializer1(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET all Examinations
@api_view(['GET'])
def get_all_examinations(request):
    examinations = Examination.objects.all()
    serializer = ExaminationSerializer(examinations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET all PatientExaminations
@api_view(['GET'])
def get_all_patient_examinations(request):
    patient_examinations = PatientExamination.objects.all()
    serializer = PatientExaminationSerializer(patient_examinations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET all ItemPatientExaminations
@api_view(['GET'])
def get_all_item_patient_examinations(request):
    item_patient_examinations = ItemPatientExamination.objects.all()
    serializer = ItemPatientExaminationSerializer(item_patient_examinations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET list of ItemPatientExaminations by PatientExamination ID
@api_view(['GET'])
def get_item_patient_examinations_by_patient_id(request, patient_examination_id):
    try:
        patient_examination = PatientExamination.objects.get(id=patient_examination_id)
    except PatientExamination.DoesNotExist:
        return Response({'error': 'PatientExamination not found'}, status=status.HTTP_404_NOT_FOUND)

    item_patient_examinations = ItemPatientExamination.objects.filter(patient_examination=patient_examination)
    serializer = ItemPatientExaminationSerializer(item_patient_examinations, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Update ItemPatientExamination
@api_view(['PUT'])
def update_item_patient_examination(request, item_id):
    try:
        item_patient_examination = ItemPatientExamination.objects.get(id=item_id)
    except ItemPatientExamination.DoesNotExist:
        return Response({'error': 'ItemPatientExamination not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ItemPatientExaminationSerializer(item_patient_examination, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete ItemPatientExamination
@api_view(['DELETE'])
def delete_item_patient_examination(request, item_id):
    try:
        item_patient_examination = ItemPatientExamination.objects.get(id=item_id)
    except ItemPatientExamination.DoesNotExist:
        return Response({'error': 'ItemPatientExamination not found'}, status=status.HTTP_404_NOT_FOUND)

    item_patient_examination.delete()
    return Response({'message': 'ItemPatientExamination deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

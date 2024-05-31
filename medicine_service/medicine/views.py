from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Producer, Medicine, PatientMedicine, ItemPatientMedicine
from .serializers import ProducerSerializer, MedicineSerializer,MedicineSerializer1, PatientMedicineSerializer, ItemPatientMedicineSerializer,ItemPatientMedicineSerializer1

# POST add Producer
@api_view(['POST'])
def add_producer(request):
    serializer = ProducerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST add Medicine
@api_view(['POST'])
def add_medicine(request):
    serializer = MedicineSerializer1(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST add PatientMedicine
@api_view(['POST'])
def add_patient_medicine(request):
    serializer = PatientMedicineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST add ItemPatientMedicine
@api_view(['POST'])
def add_item_patient_medicine(request):
    serializer = ItemPatientMedicineSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET all Producers
@api_view(['GET'])
def get_all_producers(request):
    producers = Producer.objects.all()
    serializer = ProducerSerializer(producers, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET all Medicines
@api_view(['GET'])
def get_all_medicines(request):
    medicines = Medicine.objects.all()
    serializer = MedicineSerializer(medicines, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET all PatientMedicines
@api_view(['GET'])
def get_all_patient_medicines(request):
    patient_medicines = PatientMedicine.objects.all()
    serializer = PatientMedicineSerializer(patient_medicines, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET all ItemPatientMedicines
@api_view(['GET'])
def get_all_item_patient_medicines(request):
    item_patient_medicines = ItemPatientMedicine.objects.all()
    serializer = ItemPatientMedicineSerializer(item_patient_medicines, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def get_item_patient_medicines_by_patient_id(request, patient_medicine_id):
    try:
        patient_medicine = PatientMedicine.objects.get(id=patient_medicine_id)
    except PatientMedicine.DoesNotExist:
        return Response({'error': 'PatientMedicine not found'}, status=status.HTTP_404_NOT_FOUND)

    item_patient_medicines = ItemPatientMedicine.objects.filter(patient_medicine=patient_medicine)
    serializer = ItemPatientMedicineSerializer(item_patient_medicines, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)



@api_view(['PUT'])
def update_item_patient_medicine(request, item_id):
    try:
        item_patient_medicine = ItemPatientMedicine.objects.get(id=item_id)
    except ItemPatientMedicine.DoesNotExist:
        return Response({'error': 'ItemPatientMedicine not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ItemPatientMedicineSerializer(item_patient_medicine, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete ItemPatientMedicine
@api_view(['DELETE'])
def delete_item_patient_medicine(request, item_id):
    try:
        item_patient_medicine = ItemPatientMedicine.objects.get(id=item_id)
    except ItemPatientMedicine.DoesNotExist:
        return Response({'error': 'ItemPatientMedicine not found'}, status=status.HTTP_404_NOT_FOUND)

    item_patient_medicine.delete()
    return Response({'message': 'ItemPatientMedicine deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Producer, Supply, PatientSupply, ItemPatientSupply
from .serializers import ProducerSerializer, SupplySerializer, PatientSupplySerializer, ItemPatientSupplySerializer

# POST add Producer
@api_view(['POST'])
def add_producer(request):
    serializer = ProducerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST add Supply
@api_view(['POST'])
def add_supply(request):
    serializer = SupplySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST add PatientSupply
@api_view(['POST'])
def add_patient_supply(request):
    serializer = PatientSupplySerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# POST add ItemPatientSupply
@api_view(['POST'])
def add_item_patient_supply(request):
    serializer = ItemPatientSupplySerializer(data=request.data)
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

# GET all Supplies
@api_view(['GET'])
def get_all_supplies(request):
    supplies = Supply.objects.all()
    serializer = SupplySerializer(supplies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET all PatientSupplies
@api_view(['GET'])
def get_all_patient_supplies(request):
    patient_supplies = PatientSupply.objects.all()
    serializer = PatientSupplySerializer(patient_supplies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET all ItemPatientSupplies
@api_view(['GET'])
def get_all_item_patient_supplies(request):
    item_patient_supplies = ItemPatientSupply.objects.all()
    serializer = ItemPatientSupplySerializer(item_patient_supplies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# GET list of ItemPatientSupplies by PatientSupply ID
@api_view(['GET'])
def get_item_patient_supplies_by_patient_id(request, patient_supply_id):
    try:
        patient_supply = PatientSupply.objects.get(id=patient_supply_id)
    except PatientSupply.DoesNotExist:
        return Response({'error': 'PatientSupply not found'}, status=status.HTTP_404_NOT_FOUND)

    item_patient_supplies = ItemPatientSupply.objects.filter(patient_supply=patient_supply)
    serializer = ItemPatientSupplySerializer(item_patient_supplies, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

# Update ItemPatientSupply
@api_view(['PUT'])
def update_item_patient_supply(request, item_id):
    try:
        item_patient_supply = ItemPatientSupply.objects.get(id=item_id)
    except ItemPatientSupply.DoesNotExist:
        return Response({'error': 'ItemPatientSupply not found'}, status=status.HTTP_404_NOT_FOUND)

    serializer = ItemPatientSupplySerializer(item_patient_supply, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# Delete ItemPatientSupply
@api_view(['DELETE'])
def delete_item_patient_supply(request, item_id):
    try:
        item_patient_supply = ItemPatientSupply.objects.get(id=item_id)
    except ItemPatientSupply.DoesNotExist:
        return Response({'error': 'ItemPatientSupply not found'}, status=status.HTTP_404_NOT_FOUND)

    item_patient_supply.delete()
    return Response({'message': 'ItemPatientSupply deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import InputInformation, Patient
from .serializers import InputInformationSerializer, PatientSerializer, PatientSerializer1
from django.db import IntegrityError
import requests

# POST add InputInformation


# POST add Patient
# @api_view(['POST'])
# def add_patient(request):
#     input_information_data = request.data.get('input')
#     patient_data = {
#         'title': request.data.get('title'),
#         'customer': request.data.get('customer'),
#         'doctor': request.data.get('doctor'),
#         'chanDoanLamSang': request.data.get('chanDoanLamSang'),
#         'ketQua': request.data.get('ketQua'),
#         'note': request.data.get('note'),
#         'state': request.data.get('state'),
#         'room': request.data.get('room'),
#         'bed': request.data.get('bed')
#     }

#     if not (input_information_data and patient_data['title'] and patient_data['customer'] and patient_data['doctor']):
#         return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

#     input_information_serializer = InputInformationSerializer(data=input_information_data)

#     if input_information_serializer.is_valid():
#         input_information = input_information_serializer.save()

#         patient_data['input'] = input_information.id
#         patient_serializer = PatientSerializer1(data=patient_data)

#         if patient_serializer.is_valid():
#             try:
#                 patient = patient_serializer.save()
#                 return Response(
#                     {
#                         'patient': PatientSerializer1(patient).data,
#                         'message': "Patient added successfully"
#                     },
#                     status=status.HTTP_201_CREATED
#                 )
#             except IntegrityError:
#                 return Response({'message': 'Database error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         else:
#             return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(input_information_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_patient(request):
    input_information_data = request.data.get('input')
    state = request.data.get('state')
    room = request.data.get('room')
    bed = request.data.get('bed')
    type_room = request.data.get('type_room')

    # Kiểm tra các trường bắt buộc khi state là "Noi tru"
    if state == 'Noi tru':
        if type_room is None:
            return Response({'error': 'Type room is required for inpatients.'}, status=status.HTTP_400_BAD_REQUEST)
        if room is None:
            return Response({'error': 'Room is required for inpatients.'}, status=status.HTTP_400_BAD_REQUEST)
        if bed is None:
            return Response({'error': 'Bed is required for inpatients.'}, status=status.HTTP_400_BAD_REQUEST)

    patient_data = {
        'title': request.data.get('title'),
        'customer': request.data.get('customer'),
        'doctor': request.data.get('doctor'),
        'chanDoanLamSang': request.data.get('chanDoanLamSang'),
        'ketQua': request.data.get('ketQua'),
        'note': request.data.get('note'),
        'state': state,
        'room': room,
        'type_room': type_room,
        'bed': bed
    }

    if not (input_information_data and patient_data['title'] and patient_data['customer'] and patient_data['doctor']):
        return Response({'error': 'Missing fields'}, status=status.HTTP_400_BAD_REQUEST)

    input_information_serializer = InputInformationSerializer(data=input_information_data)

    if input_information_serializer.is_valid():
        input_information = input_information_serializer.save()

        patient_data['input'] = input_information.id
        patient_serializer = PatientSerializer1(data=patient_data)

        if patient_serializer.is_valid():
            try:
                patient = patient_serializer.save()
                return Response(
                    {
                        'patient': PatientSerializer1(patient).data,
                        'message': "Patient added successfully"
                    },
                    status=status.HTTP_201_CREATED
                )
            except IntegrityError:
                return Response({'message': 'Database error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(input_information_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# GET all InputInformations

# @api_view(['PUT'])
# def update_patient(request, id):
#     patient = get_object_or_404(Patient, id=id)
#     input_information_data = request.data.get('input')
#     patient_data = {
#         'title': request.data.get('title'),
#         'customer': request.data.get('customer'),
#         'doctor': request.data.get('doctor'),
#         'chanDoanLamSang': request.data.get('chanDoanLamSang'),
#         'ketQua': request.data.get('ketQua'),
#         'note': request.data.get('note'),
#         'state': request.data.get('state'),
#         'room': request.data.get('room'),
#         'bed': request.data.get('bed'),
#         'input': patient.input.id  # Thêm dòng này để truyền khóa chính của input vào serializer
#     }

#     if not input_information_data:
#         return Response({'error': 'Missing input information'}, status=status.HTTP_400_BAD_REQUEST)

#     input_information_serializer = InputInformationSerializer(patient.input, data=input_information_data)

#     if input_information_serializer.is_valid():
#         input_information_serializer.save()

#         patient_serializer = PatientSerializer1(patient, data=patient_data)

#         if patient_serializer.is_valid():
#             try:
#                 patient_serializer.save()
#                 return Response(
#                     {
#                         'patient': PatientSerializer1(patient).data,
#                         'message': "Patient updated successfully"
#                     },
#                     status=status.HTTP_200_OK
#                 )
#             except IntegrityError:
#                 return Response({'message': 'Database error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
#         else:
#             return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#     else:
#         return Response(input_information_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def update_patient(request, id):
    patient = get_object_or_404(Patient, id=id)
    input_information_data = request.data.get('input')
    state = request.data.get('state')
    room = request.data.get('room')
    bed = request.data.get('bed')
    type_room = request.data.get('type_room')

    # Kiểm tra các trường bắt buộc khi state là "Noi tru"
    if state == 'Noi tru':
        if type_room is None:
            return Response({'error': 'Type room is required for inpatients.'}, status=status.HTTP_400_BAD_REQUEST)
        if room is None:
            return Response({'error': 'Room is required for inpatients.'}, status=status.HTTP_400_BAD_REQUEST)
        if bed is None:
            return Response({'error': 'Bed is required for inpatients.'}, status=status.HTTP_400_BAD_REQUEST)

    patient_data = {
        'title': request.data.get('title'),
        'customer': request.data.get('customer'),
        'doctor': request.data.get('doctor'),
        'chanDoanLamSang': request.data.get('chanDoanLamSang'),
        'ketQua': request.data.get('ketQua'),
        'note': request.data.get('note'),
        'state': state,
        'type_room': type_room,
        'room': room,
        'bed': bed,
        'input': patient.input.id  # Thêm dòng này để truyền khóa chính của input vào serializer
    }

    if not input_information_data:
        return Response({'error': 'Missing input information'}, status=status.HTTP_400_BAD_REQUEST)

    input_information_serializer = InputInformationSerializer(patient.input, data=input_information_data)

    if input_information_serializer.is_valid():
        input_information_serializer.save()

        patient_serializer = PatientSerializer1(patient, data=patient_data)

        if patient_serializer.is_valid():
            try:
                patient_serializer.save()
                return Response(
                    {
                        'patient': PatientSerializer1(patient).data,
                        'message': "Patient updated successfully"
                    },
                    status=status.HTTP_200_OK
                )
            except IntegrityError:
                return Response({'message': 'Database error occurred'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(patient_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response(input_information_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Get patient by customer id
@api_view(['GET'])
def get_patients_by_customer_id(request, customer_id):
    # Lấy tất cả các bản ghi Patient có customer_id cụ thể
    patients = Patient.objects.filter(customer=customer_id)
    
    # Serialize danh sách bản ghi
    serializer = PatientSerializer(patients, many=True)
    
    return Response(serializer.data, status=status.HTTP_200_OK)

# Delete patient by customer id
@api_view(['DELETE'])
def delete_patient_by_id(request, patient_id):
    try:


        patient = Patient.objects.get(id=patient_id)
    except Patient.DoesNotExist:
        # Trả về lỗi nếu không tìm thấy bản ghi
        return Response({'error': 'Patient not found'}, status=status.HTTP_404_NOT_FOUND)
    
    # Xóa bản ghi
    patient.delete()
    
    # Trả về phản hồi thành công
    return Response({'success': 'Patient deleted successfully'}, status=status.HTTP_204_NO_CONTENT)


# @api_view(['GET'])
# def get_patient_by_id(request,id):
#     patient = get_object_or_404(Patient, id=id)
#     patient_data = PatientSerializer(patient).data

#     # Lấy thông tin chi tiết của customer bằng ID
#     customer_url = f'http://127.0.0.1:9003/customer/api/get-customer-by-id/{patient.customer}/'
#     response_customer = requests.get(customer_url)
#     customer_data = response_customer.json()

#     # Lấy thông tin chi tiết của doctor bằng ID
#     doctor_url = f'http://127.0.0.1:9004/doctor/api/get-doctor-by-id/{patient.doctor}/'
#     response_doctor = requests.get(doctor_url)
#     doctor_data = response_doctor.json()

#     # Lấy thông tin chi tiết của room bằng ID
#     room_url = f'http://127.0.0.1:9002/clinic/api/get-room-by-id/{patient.room}/'
#     response_room = requests.get(room_url)
#     room_data = response_room.json()

#     # Lấy thông tin chi tiết của type room bằng ID
#     type_room_url = f'http://127.0.0.1:9002/clinic/api/get-type-room-by-id/{patient.type_room}/'
#     response_type_room = requests.get(type_room_url)
#     type_room_data = response_type_room.json()

#     # Lấy thông tin chi tiết của bed bằng ID
#     bed_url = f'http://127.0.0.1:9002/clinic/api/get-bed-by-id/{patient.bed}/'
#     response_bed = requests.get(bed_url)
#     bed_data = response_bed.json()

#     # Tạo response cho patient bao gồm các thông tin được lấy từ các service khác
#     response_patient = {
#         'patient': patient_data,
#         'customer': customer_data,
#         'doctor': doctor_data,
#         'room': room_data,
#         'type_room': type_room_data,
#         'bed': bed_data
#     }

#     return Response(response_patient, status=status.HTTP_200_OK)




@api_view(['GET'])
def get_patient_by_id(request, id):
    # Lấy thông tin của bệnh nhân
    patient = get_object_or_404(Patient, id=id)
    patient_data = PatientSerializer(patient).data

    # Lấy thông tin chi tiết của customer bằng ID
    customer_url = f'http://127.0.0.1:9003/customer/api/get-customer-by-id/{patient.customer}/'
    response_customer = requests.get(customer_url)
    customer_data = response_customer.json()

    # Lấy thông tin chi tiết của doctor bằng ID
    doctor_url = f'http://127.0.0.1:9004/doctor/api/get-doctor-by-id/{patient.doctor}/'
    response_doctor = requests.get(doctor_url)
    doctor_data = response_doctor.json()

    # Lấy thông tin chi tiết của room bằng ID
    room_url = f'http://127.0.0.1:9002/clinic/api/get-room-by-id/{patient.room}/'
    response_room = requests.get(room_url)
    room_data = response_room.json()

    # Lấy thông tin chi tiết của type room bằng ID
    type_room_url = f'http://127.0.0.1:9002/clinic/api/get-type-room-by-id/{patient.type_room}/'
    response_type_room = requests.get(type_room_url)
    type_room_data = response_type_room.json()

    # Lấy thông tin chi tiết của bed bằng ID
    bed_url = f'http://127.0.0.1:9002/clinic/api/get-bed-by-id/{patient.bed}/'
    response_bed = requests.get(bed_url)
    bed_data = response_bed.json()

    # Thêm thông tin của customer, doctor, room, type_room, và bed vào dữ liệu của patient
    patient_data['customer'] = customer_data
    patient_data['doctor'] = doctor_data
    patient_data['room'] = room_data
    patient_data['type_room'] = type_room_data
    patient_data['bed'] = bed_data

    return Response(patient_data, status=status.HTTP_200_OK)




# @api_view(['GET'])
# def get_patient_by_id(request, id):
#     # Lấy bản ghi Patient với id cụ thể
#     patient = get_object_or_404(Patient, id=id)
    
#     # Serialize bản ghi
#     serializer = PatientSerializer(patient)
    
#     return Response(serializer.data, status=status.HTTP_200_OK)
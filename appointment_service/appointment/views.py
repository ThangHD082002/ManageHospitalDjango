from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .models import Appointment
from .serializers import AppointmentSerializer, AppointmentSerializer1, PhongSerializer
from rest_framework import status

@api_view(['POST'])
def add_appointment(request):
    serializer = AppointmentSerializer1(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def add_phong(request):
    # Lấy dữ liệu từ request
    data = request.data

    # Deserialize dữ liệu vào một đối tượng PhongSerializer
    serializer = PhongSerializer(data=data)

    # Kiểm tra tính hợp lệ của dữ liệu
    if serializer.is_valid():
        # Lưu phòng vào cơ sở dữ liệu
        phong = serializer.save()

        # Trả về phản hồi thành công
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    else:
        # Trả về phản hồi lỗi nếu dữ liệu không hợp lệ
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
import requests
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import Appointment
from .serializers import AppointmentSerializer

@api_view(['GET'])
def get_appointment_by_id(request, id):
    # Lấy cuộc hẹn từ cơ sở dữ liệu
    appointment = get_object_or_404(Appointment, id=id)
    
    # Tạo URL để lấy thông tin chi tiết của bác sĩ
    doctor_url = f'http://127.0.0.1:9004/doctor/api/get-doctor-by-id/{appointment.doctor}/'
    response_doctor = requests.get(doctor_url)
    doctor_data = response_doctor.json()

    # Tạo URL để lấy thông tin chi tiết của khách hàng
    customer_url = f'http://127.0.0.1:9003/customer/api/get-customer-by-id/{appointment.customer}/'
    response_customer = requests.get(customer_url)
    customer_data = response_customer.json()

    # Tạo response mới với thông tin chi tiết của bác sĩ và khách hàng
    appointment_data = AppointmentSerializer(appointment).data
    appointment_data['doctor'] = doctor_data
    appointment_data['customer'] = customer_data

    return Response(appointment_data)



@api_view(['GET'])
def get_appointments_by_doctor_id(request, doctor_id):
    # Lấy tất cả các cuộc hẹn của bác sĩ dựa trên ID
    appointments = Appointment.objects.filter(doctor=doctor_id)

    # Tạo một danh sách để lưu trữ thông tin cuộc hẹn cập nhật với thông tin của bác sĩ và khách hàng
    updated_appointments = []

    for appointment in appointments:
        # Lấy thông tin chi tiết của bác sĩ bằng cách sử dụng request
        doctor_url = f'http://127.0.0.1:9004/doctor/api/get-doctor-by-id/{appointment.doctor}/'
        response_doctor = requests.get(doctor_url)
        doctor_data = response_doctor.json()

        # Lấy thông tin chi tiết của khách hàng bằng cách sử dụng request
        customer_url = f'http://127.0.0.1:9003/customer/api/get-customer-by-id/{appointment.customer}/'
        response_customer = requests.get(customer_url)
        customer_data = response_customer.json()

        # Tạo một dictionary mới để lưu trữ thông tin cuộc hẹn đã được cập nhật
        updated_appointment = {
            'id': appointment.id,
            'title': appointment.title,
            'timeStart': appointment.timeStart,
            'phong': appointment.phong.id,
            'state': appointment.state,
            'doctor': doctor_data,
            'customer': customer_data
        }

        updated_appointments.append(updated_appointment)

    return Response(updated_appointments, status=200)



@api_view(['GET'])
def get_all_appointments(request):
    # Lấy tất cả các cuộc hẹn từ cơ sở dữ liệu
    appointments = Appointment.objects.all()
    
    # Khởi tạo một danh sách để lưu trữ thông tin của mỗi cuộc hẹn kèm theo thông tin của bác sĩ và khách hàng
    appointment_data_list = []
    
    # Duyệt qua từng cuộc hẹn
    for appointment in appointments:
        # Lấy thông tin chi tiết của bác sĩ bằng cách gửi yêu cầu đến service doctor
        doctor_url = f'http://127.0.0.1:9004/doctor/api/get-doctor-by-id/{appointment.doctor}/'
        response_doctor = requests.get(doctor_url)
        doctor_data = response_doctor.json()

        # Lấy thông tin chi tiết của khách hàng bằng cách gửi yêu cầu đến service customer
        customer_url = f'http://127.0.0.1:9003/customer/api/get-customer-by-id/{appointment.customer}/'
        response_customer = requests.get(customer_url)
        customer_data = response_customer.json()

        # Tạo một dict mới chứa thông tin của cuộc hẹn kèm theo thông tin của bác sĩ và khách hàng
        appointment_data = {
            'id': appointment.id,
            'title': appointment.title,
            'timeStart': appointment.timeStart,
            'phong': appointment.phong.id,
            'state': appointment.state,
            'doctor': doctor_data,
            'customer': customer_data
        }

        # Thêm dict này vào danh sách
        appointment_data_list.append(appointment_data)
    
    # Trả về danh sách cuộc hẹn với thông tin đầy đủ của bác sĩ và khách hàng
    return Response(appointment_data_list)
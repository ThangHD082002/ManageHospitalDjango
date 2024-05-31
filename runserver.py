import subprocess

# Danh sách các dịch vụ và cổng tương ứng
services = [
    ("appointment_service", 9001),
    # ("clinic_service", 9002),
    ("customer_service", 9003),
    ("doctor_service", 9004),
    # ("employee_service", 9005),
    # ("medicine_service", 9006),
    # ("patient_service", 9007),
    # ("payment_service", 9008),
    # ("user_service", 9009),



]

# Duyệt qua từng dịch vụ
for service, port in services:
    print(f"Migrating {service}...")
    try:
        # Di chuyển vào thư mục dịch vụ và thực thi lệnh migrate
        subprocess.run(f"cd {service} && python manage.py makemigrations", shell=True, check=True)

        # Thực hiện các lệnh migrate đặc biệt cho từng dịch vụ
        if service == "user_service":
            subprocess.run(
                f"cd {service} && python manage.py migrate",
                shell=True,
                check=True,
            )
        elif service == "payment_service":
            subprocess.run(f"cd {service} && python manage.py migrate --database=payment_db",
                shell=True, 
                check=True
            )
        elif service == "clinic_service":
            subprocess.run(f"cd {service} && python manage.py migrate --database=clinic_db",
                shell=True, 
                check=True
            )
        elif service == "patient_service":
            subprocess.run(f"cd {service} && python manage.py migrate --database=patient_db",
                shell=True, 
                check=True
            )
        elif service == "medicine_service":
            subprocess.run(
                f"cd {service} && python manage.py migrate --database=medicine_db && \
                python manage.py migrate --database=supply_db && \
                python manage.py migrate --database=examination_db",
                shell=True, 
                check=True
            )
        elif service == "appointment_service":
            subprocess.run(f"cd {service} && python manage.py migrate --database=appointment_db",
                shell=True, 
                check=True
            )
        elif service == "customer_service":
            subprocess.run(f"cd {service} && python manage.py migrate",
                shell=True, 
                check=True
            )
        elif service == "doctor_service":
            subprocess.run(f"cd {service} && python manage.py migrate",
                shell=True, 
                check=True
            )
        elif service == "employee_service":
            subprocess.run(f"cd {service} && python manage.py migrate",
                shell=True, 
                check=True
            )

        # Khởi động server
        subprocess.Popen(f"cd {service} && python manage.py runserver {port}", shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Failed to start {service}: {e}")

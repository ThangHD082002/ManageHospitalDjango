import pymongo


def delete_databases(database_names, mongo_uri):
    # Kết nối tới MongoDB
    client = pymongo.MongoClient(mongo_uri)

    # Lặp qua từng tên database và xóa nó
    for db_name in database_names:
        client.drop_database(db_name)
        print(f"Đã xoá database '{db_name}' thành công.")


# Các cơ sở dữ liệu bạn muốn xoá
databases_to_delete = [
    "manage",
    "user",
    'payment',
    'customer',
    'doctor',
    'employee',
    'patient',
    'medicine',
    'supply',
    'examination',
    'clinic',
    'appointment',


]  # Thay đổi thành các tên database bạn muốn xoá

# URI kết nối tới MongoDB
mongo_connection_uri = "mongodb://localhost:27017/"  # Thay đổi URI nếu cần thiết

# Gọi hàm để xoá các cơ sở dữ liệu
delete_databases(databases_to_delete, mongo_connection_uri)

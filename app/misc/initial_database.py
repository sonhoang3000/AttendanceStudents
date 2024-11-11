import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://facerecognition-b74ff-default-rtdb.firebaseio.com/",
    },
)

ref = db.reference("Students")  

data = {
    "XM": { 
        "id": "XM",
        "name": "Nguyễn Thị Xuân Mai",
        "password": "XM",
        "dob": "7-03-2004",
        "address": "Quận 12",
        "phone": "123456789",
        "email": "congaxuanmai@gmail.com",
        "major": "Công Nghệ Thông Tin",
        "starting_year": 2022,
        "standing": "Hạng bét",
        "total_attendance": 4,
        "year": 3,
        "last_attendance_time": "2023-02-21 12:33:10",
        "content": "Học Viện Hàng Không",
    },
    "KN": { 
        "id": "KN",
        "name": "Nguyễn Trần Khánh Ngọc",
        "password": "KN",
        "dob": "7-03-2004",
        "address": "Quận 12",
        "phone": "123456789",
        "email": "kn@gmail.com",
        "major": "Công Nghệ Thông Tin",
        "starting_year": 2022,
        "standing": "Hạng A",
        "total_attendance": 4,
        "year": 3,
        "last_attendance_time": "2023-02-21 12:33:10",
        "content": "Học Viện Hàng Không",
    },
     "HS": { 
        "id": "HS",
        "name": "Vũ Hoàng Sơn",
        "password": "HS",
        "dob": "7-03-2004",
        "address": "Tân Phú",
        "phone": "123456789",
        "email": "hs@gmail.com",
        "major": "Công Nghệ Thông Tin",
        "starting_year": 2022,
        "standing": "Hạng A",
        "total_attendance": 4,
        "year": 3,
        "last_attendance_time": "2023-02-21 12:33:10",
        "content": "Học Viện Hàng Không",
    },
     "MD": { 
        "id": "MD",
        "name": "Lê Minh Đức",
        "password": "MD",
        "dob": "7-03-2004",
        "address": "Tân Phú",
        "phone": "123456789",
        "email": "MD@gmail.com",
        "major": "Công Nghệ Thông Tin",
        "starting_year": 2022,
        "standing": "Hạng A",
        "total_attendance": 4,
        "year": 3,
        "last_attendance_time": "2023-02-21 12:33:10",
        "content": "Học Viện Hàng Không",
    },
    "QA": { 
        "id": "QA",
        "name": "Quốc Anh",
        "password": "QA",
        "dob": "7-03-2004",
        "address": "Tân Phú",
        "phone": "123456789",
        "email": "qa@gmail.com",
        "major": "Công Nghệ Thông Tin",
        "starting_year": 2022,
        "standing": "Hạng A",
        "total_attendance": 4,
        "year": 3,
        "last_attendance_time": "2023-02-21 12:33:10",
        "content": "Học Viện Hàng Không",
    }   
}
for key, value in data.items():
    ref.child(key).set(value)

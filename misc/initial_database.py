import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(
    cred,
    {
        "databaseURL": "https://facerecognition-b74ff-default-rtdb.firebaseio.com/",
        # database URL
    },
)

ref = db.reference(
    "Students"
)  # reference path to our database... will create student directory in the database

data = {
    "004223": {  # id of student which is a key
        "id": "004223",
        "name": "Samrat Thapa",
        "password": "004223Samrat",
        "dob": "1997-08-02",
        "address": "Barrie, Ontario",
        "phone": "2348657951",
        "email": "samratthapa@gmail.com",
        "major": "Data Science",
        "starting_year": 2020,
        "standing": "G",
        "total_attendance": 4,
        "year": 2,
        "last_attendance_time": "2023-02-21 12:33:10",
        "content": "This section aims to offer essential guidance for students to successfully complete the course. It will be regularly updated \
                to ensure its relevance and usefulness. Stay tuned for valuable \
                insights and tips that will help you excel in your studies.",
    },
    "135795": { 
        "id": "135795",
        "name": "Nguyễn Thị Xuân Mai",
        "password": "135795",
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
        "content": "Dù cuộc sống có ra sao, tao vẫn mãi bịp vì tao là vua bịp, You shold know me who is BỊP THỦ",
    },
}


for key, value in data.items():
    ref.child(key).set(value)

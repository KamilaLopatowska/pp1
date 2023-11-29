import json
student_data = {
    "name" : "Kamila",
    "surname" : "Łopatowska",
    "nr albumu": "231171",
    "kierunek" : "informatyka stosowana",
    "semestr" : 1,

}

with open('student.json', 'w', encoding = 'utf-8') as file:
    json.dump(student_data, file, indent = 4)
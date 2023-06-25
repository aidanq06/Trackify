from tkinter import *
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://RRHSfbla2023:IheBcYm1ZbOEephx@fbla2023project.wdozi9i.mongodb.net/?retryWrites=true&w=majority")
db = cluster["RRHSfbla2023"]
student_info = db["student_info"]
event_info = db["event_info"]
login_info = db["login_info"]
request_info = db["request_info"]


first_names = ["Emma", "Liam", "Olivia", "Noah", "Ava", "Isabella", "Sophia", "Mia", "Charlotte", "Amelia", "Harper", "Evelyn", "Abigail", "Emily", "Elizabeth", "Mila", "Ella", "Avery", "Sofia", "Camila", "Aria", "Scarlett", "Victoria", "Madison", "Luna", "Grace", "Chloe", "Penelope", "Layla", "Riley", "Zoey", "Nora", "Lily", "Eleanor", "Hannah", "Lillian", "Addison", "Aubrey", "Ellie", "Stella", "Natalie", "Zoe", "Leah", "Hazel", "Violet", "Aurora", "Savannah", "Audrey", "Brooklyn", "Bella", "Claire", "Skylar", "Lucy", "Paisley", "Everly", "Anna", "Caroline", "Nova", "Genesis", "Emilia", "Kennedy", "Samantha", "Maya", "Willow", "Kinsley", "Naomi", "Aaliyah", "Elena", "Sarah", "Ariana", "Allison", "Gabriella", "Alice", "Madelyn", "Cora", "Ruby", "Eva", "Serenity", "Autumn", "Adeline", "Hailey", "Gianna", "Valentina", "Isla", "Eliana", "Quinn", "Nevaeh", "Ivy", "Sadie", "Piper", "Lydia", "Alexa", "Josephine", "Emery", "Julia"]
last_names = ["Smith", "Johnson", "Williams", "Brown", "Jones", "Garcia", "Miller", "Davis", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson", "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker", "Young", "Hall", "Allen", "Wright", "King", "Scott", "Green", "Baker", "Adams", "Nelson", "Hill", "Campbell", "Mitchell", "Roberts", "Carter", "Phillips", "Evans", "Turner", "Torres", "Parker", "Collins", "Edwards", "Stewart", "Flores", "Morris", "Nguyen", "Murphy", "Rivera", "Cook", "Rogers", "Morgan", "Peterson", "Cooper", "Reed", "Bailey", "Bell", "Gomez", "Kelly", "Howard", "Ward", "Cox", "Diaz", "Richardson", "Wood", "Watson", "Brooks", "Bennett", "Gray", "James", "Reyes", "Cruz", "Hughes", "Price", "Myers", "Long", "Foster", "Sanders", "Ross", "Morales", "Powell", "Sullivan", "Russell", "Ortiz", "Jenkins"]
grades = [9, 9, 11, 12, 10, 9, 9, 11, 11, 10, 12, 9, 12, 10, 11, 10, 10, 11, 11, 10, 9, 11, 12, 11, 11, 12, 9, 11, 10, 9, 12, 9, 10, 11, 10, 12, 9, 10, 9, 11, 9, 9, 12, 11, 11, 12, 10, 9, 12, 9, 11, 10, 10, 11, 12, 11, 11, 12, 10, 10, 10, 10, 11, 10, 12, 10, 11, 12, 9, 10, 12, 10, 10, 11, 9, 10, 12, 12, 9, 9, 9, 10, 11, 10, 11, 11, 9, 10, 11, 9, 10, 9, 12, 11, 12]
points = [65, 90, 115, 175, 190, 80, 185, 160, 135, 125, 200, 235, 220, 150, 210, 205, 100, 155, 75, 135, 85, 185, 105, 220, 110, 80, 140, 185, 230, 230, 105, 70, 145, 125, 165, 110, 175, 135, 55, 80, 235, 80, 100, 80, 70, 170, 155, 125, 160, 115, 185, 70, 235, 60, 205, 175, 200, 110, 215, 140, 155, 135, 75, 120, 80, 110, 215, 65, 185, 215, 70, 140, 120, 120, 90, 175, 220, 60, 195, 100, 70, 175, 235, 85, 230, 230, 95, 120, 170, 90, 75, 125, 155, 180, 115]
studentid = [24771, 78882, 56194, 27683, 64452, 33376, 42963, 82629, 57092, 71445, 50364, 75226, 43547, 94139, 93454, 60756, 40798, 28856, 26675, 53172, 62288, 97244, 69578, 45765, 68960, 13884, 97606, 23123, 79589, 91853, 10617, 71382, 77901, 10641, 72584, 34745, 64861, 28726, 47475, 49852, 61202, 16533, 62493, 73140, 64759, 12136, 76306, 27194, 90328, 36608, 17401, 35449, 67423, 99638, 55071, 55804, 15906, 27442, 28968, 11052, 30489, 29537, 28544, 26954, 84957, 70858, 66963, 46775, 86785, 48957, 30611, 23272, 32040, 22629, 37156, 91173, 91347, 30637, 30892, 92512, 79797, 20140, 60962, 80003, 10029, 45816, 32474, 55326, 46706, 16229, 67029, 56175, 15483, 20410, 79820]


'''for i in range(len(points)):
    temp = {"_id": studentid[i], "first_name": first_names[i], "last_name": last_names[i], "grade": grades[i], "point": points[i]}
    student_info.insert_one(temp)'''
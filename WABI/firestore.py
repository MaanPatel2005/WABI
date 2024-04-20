import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("WABI\\serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection('users').add({'name': "Purav Patel", 'email': "puravp@uci.edu", 'weight': 140, 'height': 70, 'distance': 0, 'Kcal': 0, 'steps':0})
db.collection('users').add({'name': "Maan Patel", 'email': "maanvp@uci.edu", 'weight': 160, 'height': 68, 'distance': 0, 'Kcal': 0, 'steps':0})
db.collection('users').add({'name': "Dhruv Patel", 'email': "axiong4@uci.edu", 'weight': 135, 'height': 70, 'distance': 0, 'Kcal': 0, 'steps':0})
db.collection('users').add({'name': "Maan Patel", 'email': "dhruvp@uci.edu", 'weight': 160, 'height': 72, 'distance': 0, 'Kcal': 0, 'steps':0})

# users_ref = db.collection("users")
# docs = users_ref.stream()

# for doc in docs:
#     print(f"{doc.id} => {doc.to_dict()}")
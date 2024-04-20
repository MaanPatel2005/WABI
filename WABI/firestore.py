import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


cred = credentials.Certificate("WABI\\serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

db.collection('users').add({'name': "Purav Patel", 'email': "puravp@uci.edu"})
# users_ref = db.collection("users")
# docs = users_ref.stream()

# for doc in docs:
#     print(f"{doc.id} => {doc.to_dict()}")
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter


cred = credentials.Certificate("WABI\\serviceAccountKey.json")
firebase_admin.initialize_app(cred)


class Login:
    user = ""
    def __init__(self, username: str, password: str):
        self.db = firestore.client()
        self.username = username
        self.password = password
    
    def sign_in(self) -> str:
        self.db = firestore.client()
        query = self.db.collection('users').where(filter=FieldFilter('username', "==", self.username))
        query = query.where(filter=FieldFilter('password', '==', self.password))
        docs = query.stream()
        try:
            nextelem = next(docs)
            if nextelem is not None:
                return self.username
            else:
                print("Wasn't successful login")
                return None
        except:
            print("Wasn't successful login")
            return None
        

        

def sign_up(email: str, password: str, name: str, username: str, height: int, weight: int, steps: int, distance: int, calories: int, points: int, animal: str):
    db = firestore.client()

    doc_ref = db.collection('users').document(username)

    data = {
        'name': name, 
        'email': email, 
        'password': password, 
        'username': username, 
        'height': height, 
        'weight': weight,
        'steps': 0,
        'distance': 0,
        'calories' : 0,
        'point' : 0,
        'animal': "animal"
    }

    doc_ref.set(data)

    return username


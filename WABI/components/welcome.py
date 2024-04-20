import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
from google.cloud.firestore_v1.base_query import FieldFilter


cred = credentials.Certificate("WABI\\serviceAccountKey.json")
firebase_admin.initialize_app(cred)


class Login:
    def __init__(self, username: str, passkey: str):
        self.db = firestore.client()
        self.username = username
        self.passkey = passkey
    
    def sign_in(self) -> str:
        self.db = firestore.client()
        query = self.db.collection('users').where(filter=FieldFilter('username', "==", self.username))
        query = query.where(filter=FieldFilter('passkey', '==', self.passkey))
        docs = query.stream()
        try:
            nextelem = next(docs)
            if nextelem is not None:
                return self.username
            else:
                return None
        except:
            return None
        

        

def sign_up(email: str, passkey: str, name: str, username: str, height: int, weight: int):
    db = firestore.client()

    doc_ref = db.collection('users').document(username)

    data = {
        'name': name, 
        'email': email, 
        'passkey': passkey, 
        'username': username, 
        'height': height, 
        'weight': weight
    }

    doc_ref.set(data)

    return username


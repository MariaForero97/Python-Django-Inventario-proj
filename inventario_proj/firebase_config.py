import firebase_admin
from firebase_admin import credentials, firestore

# Inicializar Firebase sólo una vez
cred = credentials.Certificate("firebase_key.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

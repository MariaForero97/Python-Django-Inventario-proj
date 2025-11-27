import os
import firebase_admin
from firebase_admin import credentials, firestore

# Ruta hacia la llave
KEY_PATH = os.path.join(os.path.dirname(__file__), "firebase_key.json")

db = None  # Valor por defecto

# Solo inicializa Firebase si existe la llave
if os.path.exists(KEY_PATH):
    try:
        cred = credentials.Certificate(KEY_PATH)
        firebase_admin.initialize_app(cred)
        db = firestore.client()
    except Exception as e:
        print("Error al inicializar Firebase:", e)
        db = None

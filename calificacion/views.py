from django.shortcuts import render, redirect
from .models import Calificacion
from .forms import CalificacionForm
from inventario_proj.firebase_config import db

def home(request):
    if request.method == 'POST':
        form = CalificacionForm(request.POST)
        if form.is_valid():

            data = form.cleaned_data
            accion = request.POST.get("accion")

            # Guardar en SQLite
            if accion == "local":
                form.save()
                return redirect('calificacion:lista')

            # Guardar en Firebase (solo si db existe)
            if accion == "firebase":
                if db is not None:
                    db.collection("calificaciones").add({
                        "nombre": data["nombre"],
                        "comentario": data["comentario"],
                        "calificacion": data["calificacion"]
                    })
                else:
                    print("Firebase no está disponible en producción.")
                return redirect('calificacion:lista')

    else:
        form = CalificacionForm()

    return render(request, 'calificacion/formulario.html', {'form': form})


def lista_calificaciones(request):
    calificaciones = Calificacion.objects.all()
    return render(request, 'calificacion/lista.html', {'calificaciones': calificaciones})


def lista_firebase(request):
    if db is None:
        return render(request, "calificacion/lista_firebase.html", {
            "calificaciones": [],
            "error": "Firebase no está disponible en producción."
        })

    documentos = db.collection("calificaciones").get()
    calificaciones = [doc.to_dict() for doc in documentos]

    return render(request, "calificacion/lista_firebase.html", {
        "calificaciones": calificaciones,
        "error": None
    })

from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Notificaciones activas</h1><a href='/'>Volver</a>")
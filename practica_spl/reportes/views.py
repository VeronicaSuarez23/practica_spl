from django.http import HttpResponse

def inicio(request):
    return HttpResponse("<h1>Reporte generado</h1><a href='/'>Volver</a>")
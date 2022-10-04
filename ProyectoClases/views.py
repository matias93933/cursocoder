from multiprocessing import context
from re import template
from django.http import HttpResponse
from datetime import  datetime 
from django.template import Context, Template

def hola(request):
    return HttpResponse("<h1> Nacho boton sos amigo de la yuta , Milu te rompo toda <3 </h1> ")

def fecha(request):
    fecha_actual = datetime.now()
    return HttpResponse(f"La fecha actual es : {fecha_actual}")

def fecha_nacimiento(request, edad):
    fecha = datetime.now().year - edad
    return HttpResponse(f"Tu fecha de nacimiento es : {fecha} y tu edad es {edad} años")

def mi_template(request):
    cargar_archivo = open(r'C:\Users\Matias\Desktop\Proyecto-Coder\Templates\template.html', 'r')
    template = Template(cargar_archivo.read())
    cargar_archivo.close()
    contexto = Context()
    template_render = template.render(contexto)
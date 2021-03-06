# coding: utf-8
import pilasengine

pilas=pilasengine.iniciar()
pilas.fondos.Tarde()

titulo=pilas.actores.Texto(u"Área de un cubo", y=200, magnitud=30)
descri=u"""Para calcular el área de un cubo lo que se necesita es conocer la longitud de uno de sus lados y luego aplicar la fórmula:
  lxlxlxl
"""
parrafo1=pilas.actores.Texto(descri, y=170, ancho=400)
parrafo1.centro_y ='arriba'

etiqueta1=pilas.actores.Texto("lado=",y=-5,x=-200)
etiqueta1.centro_X='iquierda'
entrada=pilas.interfaz.IngresoDeTexto(texto='0',y=-5,x=-110,ancho=50)
entrada.centro_x='izquierda'

area=0
def calcular_area():
    lado=int(entrada.texto)
    area=lado*lado*lado
    asistente.decir(u"Área="+str(area))
    asistente.sonreir()
    
boton=pilas.interfaz.Boton("calcular")
boton.y=-8
boton.escala=1.5
boton.conectar(calcular_area)
    
asistente=pilas.actores.Mono(225,-150)
asistente.escala=1
    
pilas.ejecutar()
    
    
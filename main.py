import math


class Punto:
    def __init__(self,x,y):
        self.x=x
        self.y=y

class Forma():

    def __init__(self,punto,color,nombre):
        self.Coordenada=punto
        self.color=color
        self.nombre=nombre

    def imprimir(self):
        print("Nombre "+self.nombre+" Color -> " + self.color +" Punto -> x -> " + str(self.Coordenada.x) +" y -> "+str(self.Coordenada.y))

    def Obtener(self):
        return self.color,self.nombre,self.Coordenada.x,self.Coordenada.y

    def cambiaColor(self,color):
        self.color=color

    def moverForma(self,punto):
        self.Coordenada=punto

class Rectangulo(Forma):

    def __init__(self,punto,color,nombre,ladoMenor,ladoMayor):
        super().__init__(punto,color,nombre)
        self.ladoMenor=ladoMenor
        self.ladoMayor=ladoMayor

    def imprimir(self):
        super().imprimir()
        print("LadoMayor --> "+str(self.ladoMayor)+" LadoMenor --> "+str(self.ladoMenor))

    def area(self):
        return (self.ladoMenor*self.ladoMayor)

    def perimetro(self):
        return (2*self.ladoMenor+2*self.ladoMayor)

    def tamano(self,escala):
        self.ladoMayor=self.ladoMayor*escala
        self.ladoMenor=self.ladoMenor*escala

class Elipse(Forma):

    def __init__(self,punto,color,nombre,radioMenor,radioMayor):
        super().__init__(punto,color,nombre)
        self.radioMenor=radioMenor
        self.radioMayor=radioMayor

    def areaElipse(self):
        super().imprimir()
        area=math.pi*self.radioMayor*self.radioMenor
        print("Area de la elipse "+str(area))

class Cuadrado(Rectangulo):

    def __init__(self,punto,color,nombreForma,ladoMayor,ladoMenor):
        super().__init__(punto,color,nombreForma,ladoMayor,ladoMenor)

class Circulo(Elipse):

    def __init__(self,punto,color,nombreForma,radioMenor,radioMayor):
        super().__init__(punto,color,nombreForma,radioMenor,radioMayor)



print("----------------------FORMA1------------")
Punto1=Punto(1,3)
Forma1=Forma(Punto1,"Rojo","Cuadrado")
Punto3=Punto(10,5)
Forma1.imprimir()
Forma1.moverForma(Punto3)
Forma1.imprimir()
Forma1.cambiaColor("Azul")
Forma1.imprimir()

print("----------------------Rectangulo------------------")
Rectangulo1 = Rectangulo(Punto1,"Amarillo","Rectangulo",3,4)
Punto2=Punto(4,2)
Punto3=Punto(5,5)
Rectangulo1.imprimir()
print("Area rectángulo "+str(Rectangulo1.area()))
print("Perimetro Rectángulo "+str(Rectangulo1.perimetro()))
Rectangulo1.tamano(0.5)
Rectangulo1.imprimir()
Rectangulo1.moverForma(Punto3)
Rectangulo1.imprimir()

print("-------------------------Elipse---------------------------")
Elipse1 = Elipse(Punto1,"Verde","Elipse",5,10)
Elipse1.imprimir()


print("---------------------------Circulo--------------------------")
Circulo1=Circulo(Punto3,"Amarillo","Circulo",15,8)
Circulo1.imprimir()

print("------------------Tuplas------------------------------------")
tupla=(Forma1,Rectangulo1,Elipse1,Circulo1)
x=5
y=4
for formasLista in tupla:
    formasLista.color="Blanco"
    PuntoDinamico=Punto(x,y)
    formasLista.moverForma(PuntoDinamico)
    x=x+1
    y=y+1
    formasLista.imprimir()
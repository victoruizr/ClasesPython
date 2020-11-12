
class Empleado():
    def __init__(self,nombre,apellidos,DNI,direccion,antiguedad,tlf,salario,supervisor,puesto):
        self.nombre=nombre
        self.apellidos=apellidos
        self.DNI=DNI
        self.direccion=direccion
        self.antiguedad=antiguedad
        self.telefono=tlf
        self.salario=salario
        self.supervisor=supervisor
        self.puesto=puesto
    def imprimir(self):
        print(
              " Nombre --> "+self.nombre+
              " Apellidos --> "+ self.apellidos+
              " DNI --> "+self.DNI+
              " Direccion --> "+self.direccion+
              " Antiguedad --> "+self.antiguedad+
              " Telefono --> "+self.telefono+
              " Salario --> "+str(self.salario)+"€"+
              " Supervisor Nombre --> "+self.supervisor.nombre+
              " Apellidos --> "+self.supervisor.apellidos+
              " Puesto --> "+self.puesto)

    def cambiarSupervisor(self,supervisor):
        self.supervisor=supervisor

    def aumentarSalario(self,salario):
        self.salario+=salario

class Secretario(Empleado):

    def __init__(self,nombre,apellidos,DNI,direccion,antiguedad,tlf,salario,supervisor,puesto,fax,despacho):
        super().__init__(nombre,apellidos,DNI,direccion,antiguedad,tlf,salario,supervisor,puesto)
        self.fax=fax
        self.despacho=despacho
        self.salario=self.salario+(self.salario*0.05)

    def imprimr(self):
        super().imprimir()
        print(" Fax --> "+self.fax+" Despacho --> "+self.despacho)

class Cliente():
    def __init__(self,nombre,apellidos,DNI):
        self.nombre=nombre
        self.apellidos=apellidos
        self.DNI=DNI

class Coche():
    def __init__(self,marca,modelo,matricula):
        self.marca=marca
        self.modelo=modelo
        self.matricula=matricula

class Vendedor(Empleado):
    def __init__(self,nombre,apellidos,DNI,direccion,antiguedad,tlf,salario,supervisor,puesto,coche,areaVenta,listaClientes,porcentaje):
        super().__init__(nombre,apellidos,DNI,direccion,antiguedad,tlf,salario,supervisor,puesto)
        self.coche=coche
        self.areaVenta=areaVenta
        self.listaClientes=listaClientes
        self.porcentajes=porcentaje
        self.salario+=self.salario+(self.salario*0.10)

    def imprimirLista(self):
       for l in self.listaClientes:
           print('%s - %s' % (l.nombre, l.apellidos))

    def aumentarSalario(self,salario):
        self.salario+=salario

    def imprimr(self):
         super().imprimir()
         print(" Marca --> "+self.coche.marca+" Modelo --> "+self.coche.modelo+
         " Area venta --> "+self.areaVenta+" Porcentaje "+self.porcentajes+" Puesto --> "+self.puesto)
         print("Lista clientes --> ")
         self.imprimirLista()

    def altaCliente(self,cliente):
        self.listaClientes.append(cliente)

    def bajaCliente(self,nombre):
        i=0
        for elements in self.listaClientes:
            if elements.nombre == nombre:
                self.listaClientes.pop(i)
            i+=1

    def cambiaCoche(self,coche):
        self.coche=coche


class jefeZona(Empleado):
    def __init__(self, nombre, apellidos, DNI, direccion, antiguedad, tlf, salario,supervisor,puesto,secretario,listaVendedores,coche,despacho):
        super().__init__(nombre, apellidos, DNI, direccion, antiguedad, tlf, salario,supervisor,puesto)
        self.secretario=secretario
        self.listaVendedores=listaVendedores
        self.salario=self.salario+(self.salario*0.20)
        self.coche=coche
        self.despacho=despacho
        self.puesto=puesto

    def imprimirLista(self):
        for l in self.listaVendedores:
            print('%s - %s' % (l.nombre, l.apellidos))

    def imprimr(self):
       print(" Secretario  Nombre --> " + self.secretario.nombre+" Despacho --> "+self.despacho+" Marca --> "+self.coche.marca+" Modelo --> "+self.coche.modelo+
       "Matricula --> "+self.coche.matricula
       )
       print("Lista vendedores --> ")
       self.imprimirLista()

    def cambioSecretario(self,secretario):
        self.secretario=secretario

    def cambiaCoche(self, coche):
        self.coche=coche

    def altaVendedor(self,vendedor):
        self.listaVendedores.append(vendedor)

    def bajaVendedor(self,nombre):
        i=0
        for elements in self.listaVendedores:
            if elements.nombre == nombre:
                self.listaVendedores.pop(i)
            i+=1

print("-------------------Empleado-------------------")
Emp1=Empleado("Pepe","Ruiz","77558375","Espapa","2 años","658958",66660,Empleado,"Administrador")
Emp3=Empleado("Alex","Rodriguez","77558375","Espapa","2 años","658958",66660,Empleado,"Admintrador Sistemas")
Emp2=Empleado("Jose","Ruiz","848484","España","3 años","95840",87,Emp1,"Adminitrasdor Informatico")
Emp2.imprimir()
Emp2.cambiarSupervisor(Emp3)
Emp2.imprimir()
Emp2.aumentarSalario(20)
Emp2.imprimir()

print("--------------------------Secretario---------------")
Secretario1=Secretario("Joselito","Mendoza","8859858","Granada","2 años","62548",55,Emp1,"Jefe Sucursal","87878","Hola")
Secretario1.imprimir()

Secretario2=Secretario("Pepito","Mendoza","8859858","Granada","2 años","62548",55,Emp1,"Jefe Sucursal","87878","Hola")

Cl1=Cliente("Pepillo","Rodriguez","8484")
CL2=Cliente("Joselillo","Ruiz","475")
CL3=Cliente("Alexander","Rodriguez","4655")

lista=[Cl1,CL2]

co1=Coche("Audi","A7","8544G")
co2=Coche("Ferrari","FFX","8484Q")



print("----------------------VENDEDOR-----------------------")
Vendedor1=Vendedor("Victor","Ruiz","8859858","Granada","2 años","62548",1,Emp1,"Gerente Tienda",co1,"España",lista,"5%")
Vendedor1.imprimr()
Vendedor1.altaCliente(CL3)
Vendedor1.imprimr()
Vendedor1.bajaCliente("Alexander")
Vendedor1.imprimr()
Vendedor1.cambiaCoche(co2)
Vendedor1.imprimr()
Vendedor2=Vendedor("ABCD","Ruiz","8859858","Granada","2 años","62548",1,Emp1,"Gerente Tienda",co1,"España",lista,"5%")


lista=[Vendedor1]
print("-------------------------JEFEZONA-----------------------")
jefeZona1=jefeZona("Angelito","Manuel","7755856","Direccion","5 años","54654",5,Emp3,"Alcalde",Secretario1,lista,co1,"asdawd")
jefeZona1.imprimr()
jefeZona1.cambioSecretario(Secretario2)
jefeZona1.imprimr()
jefeZona1.altaVendedor(Vendedor2)
jefeZona1.imprimr()
jefeZona1.bajaVendedor("ABCD")
jefeZona1.imprimr()



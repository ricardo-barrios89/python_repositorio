import csv

Contacto = {'nombre':[],'apellido':[],'tel_fij':[],'tel_cel':[],'direccion':[]}
Agenda = []

def opcionMenuPrincipal():
    opt = input ("Opciones\n"
           "  1. ¿Desea agregar un contacto a su agenda?\n"
           "  2. ¿Desea buscar algun contacto de su agenda?\n"
           "  3. ¿Desea editar algun contacto de su agenda?\n"
           "  4. ¿Desea eliminar algun contacto de la agenda?\n"
           "  5. ¿Desea mostrar todos los contactos de su agenda\n"
           "  6. ¿Desea salir de la agenda?\n"
           "Escoja una opcion: ")
    return opt


def agregarContactoenAgenda(nombre,apellido,tel_fij,tel_cel,direccion):
    Contacto['nombre'].append(nombre)
    Contacto['apellido'].append(apellido)
    Contacto['tel_fij'].append(tel_fij)
    Contacto['tel_cel'].append(tel_cel)
    Contacto['direccion'].append(direccion)
    Agenda.append(Contacto)
    mostrarAgenda()


def menuAgregarContacto():
    nombre = input("Nombre: ")
    apellido = input("Apellido: ")
    tel_fij = input("Telefono fijo: ")
    tel_cel = input("Telefono celular: ")
    direccion = input("Direccion: ")
    agregarContactoenAgenda(nombre,apellido,tel_fij,tel_cel,direccion)
    ejecutarMenu()

 
def menuBuscarContacto():
    nombre = input ("Escriba el nombre del contacto: ")
    if buscarContactoPorNombre(nombre):
        mostrarContactoPorNombre(nombre)
    else:
        print("Contacto no encontrado")
    opcionMenuPrincipal()


def buscarContactoPorNombre(nombreBuscado):
    for elemento in Contacto['nombre']:
        if nombreBuscado==elemento:
            validarBusqueda=True
        else:
            validarBusqueda=False
    return validarBusqueda

    
def mostrarContactoPorNombre(nombre):
    indice=Contacto['nombre'].index(nombre)
    mostrarContactoPorIndice(indice)


def mostrarContactoPorIndice(indice):
    print(Contacto['nombre'][indice],Contacto['apellido'][indice],Contacto['tel_fij'][indice],Contacto['tel_cel'][indice],Contacto['direccion'][indice])


def eliminarContacto():
    return "eliminar contacto"


def menuEditarContacto():
    nombre = input("Escriba el nombre del contacto: ")
    if buscarContactoPorNombre(nombre):
        opMenu=menuEdicion()
    else:
        print ("Contacto no encontrado")
    mostrarAgenda()
    opcionMenuPrincipal()


def menuEdicion():
    print("*****MENU DE EDICION*****")
    optEd = input("1. Editar nombre\n2. Editar apellido\n3. Editar telefono fijo\n4. Editar telefono celular\n5. Editar direccion\nEscja una opcion: ")
    return optEd


def validarMenuEdicion(edMenu):
    optMenuEd = {}


def editarContacto(nombre):
    indice = Contacto['nombre'].index(nombre)
    Contacto['nombre'][indice] = input("Nombre: ")
    Contacto['apellido'][indice] = input("Apellido: ")
    Contacto['tel_fij'][indice] = input("Telefono fijo: ")
    Contacto['tel_cel'][indice] = input("Telefono celular: ")
    Contacto['direccion'][indice] = input("Direccion: ")
    

def mostrarAgenda():
    for contacto in Agenda:
        print (contacto)
    return "agenda mostrada"


def validarOpcionMenu(opcion):
    opcionList={ '1': menuAgregarContacto,
                 '2': menuBuscarContacto,
                 '3': menuEditarContacto,
                 }
    opt=opcionList.get(opcion, "Opcion no encontrada")
    return opt()


def validarOpcionSalirdelMenu(opcion):
    opciontList={ '1': ' ' , '2': opcionMenuPrincipal,}
    opt=opcionList.get(opcion, "Opcion no encontrada")
    return opt()


def ejecutarMenu():
    opcion=opcionMenuPrincipal()
    validarOpcionMenu(opcion)

    
if __name__ == '__main__':
    print ("********AGENDA PARA CREAR CONTACTOS********\n")
    ejecutarMenu()
    
    

    

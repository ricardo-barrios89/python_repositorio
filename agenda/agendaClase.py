class Contacto:
    def __init__(self,ced,name,last_name,house_phone,mobile_phone,address):
        self._cedula = ced
        self._nombre = name
        self._apellido = last_name
        self._tel_casa = house_phone
        self._tel_cel = mobile_phone
        self._direccion = address


    def getDato(self, n):
        if n == '1':
            return self._ced
        elif n == '2':
            return self._nombre
        elif n == '3':
            return self._apellido
        elif n == '4':
            return self._tel_casa
        elif n == '5':
            return self._tel_cel
        elif n == '6':
            return self._direccion
        else:
            return 'atributo no valido'


    def setDato(self, n, nuevo_valor):
        if n == '1':
            self._ced = nuevo_valor
        elif n == '2':
            self._nombre = nuevo_valor
        elif n == '3':
            self._apellido = nuevo_valor
        elif n == '4':
            self._tel_casa = nuevo_valor
        elif n == '5':
            self._tel_cel = nuevo_valor
        elif n == '6':
            self._direccion = nuevo_valor
        else:
            return 'atributo no valido'
        


class Agenda:
    def __init__(self):
        self._Contactos = []


    def getContacto(self, ced):
        try:
            indice_contacto=self._Contactos.index(ced)
            return Contacto[indice_contacto]
        except ValueError:
            return None

    def getListaContactos(self):
        for contacto in self._Contactos:
            return contacto

    
    def setContacto(self, contacto):
        self._Contactos.append(contacto)




 

        
class Menu:
    def __init__(self):
        print("*********AGENDA DE CONTACTOS***********")


    def menuAgenda(self):
        option = input('''Opciones
             1. - Agregar un contacto a su agenda
             2. - Buscar algun contacto de su agenda
             3. - Editar algun contacto de su agenda
             4. - Eliminar algun contacto de la agenda
             5. - Mostrar todos los contactos de su agenda
             6. - Salir de la agenda\nEscoja una opcion: ''')
        return option

    def opcionBusquedaContacto(self):
        pass


    def agregarContacto(self, agenda):
        cedula = input('CEDULA: ')
        nombre = input('NOMBRE: ')
        apellido = input('APELLIDO: ')
        tel_fij = input('TELEFONO FIJO: ')
        tel_cel = input ('TELEFONO CELULAR: ')
        direccion = input('DIRECCION: ')
        contacto = Contacto(cedula,nombre,apellido,tel_fij,tel_cel,direccion)
        agenda.setContacto(contacto)




if __name__ == '__main__':
    agenda = Agenda()
    menuAgenda = Menu()
    opcion=menuAgenda.menuAgenda()
    while opcion != '6':
        if opcion == '1':
            menuAgenda.agregarContacto(agenda)
            opcion=menuAgenda.menuAgenda()
        elif opcion == '2':
            cedula = input('CEDULA: ')
            if agenda.getContacto(cedula)==None:
                print('CONTACTO NO ENCONTRADO')
            else:
                print(agenda.getContacto(cedula))
            opcion=menuAgenda.menuAgenda()
        elif opcion == '3':
            break
        elif opcion == '4':
            break
        elif opcion == '5':
            print (agenda.getListaContactos())
        else:
            print("OPCION NO VALIDA >:V")
            opcion=menuAgenda.menuAgenda()
            

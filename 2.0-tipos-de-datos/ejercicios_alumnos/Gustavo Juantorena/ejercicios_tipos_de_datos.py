# -*- coding: utf-8 -*-
''''Tuplas, listas y diccionarios - Estructuras de control de flujo, Bucles
# Escribir un listado de famosos en un archivo .py. Desde otro archivo mostrar por pantalla el listado de famosos numerados.
#Esta hecho en dos arhivos separados
#####################################################################################################################################################################################################
# Se requiere ingresar por pantalla notas de alumnos y sus respectivos nombres. Los nombres deberán contener minimamente 5 caracteres y su nota será entre 0 y 10.
Es necesario calcular el promedio de los alumnos.
def promedio(nota):
    promedio = (sum(nota) / len(nota))
    return 'El promedio de las notas es: ' + str(promedio)
def entrada_boletin(otro_dato):
    nombre = input('ingrese el nombre del alumno. Minimo 5 caracteres\n')
    if len(nombre) > 4:
        nota = input('ingrese la nota del alumno con un valor entre 0 y 10\n')
        nota = int(nota)
        if -1 < nota < 11:
            nota = int(nota)
            boletin[nombre] = nota
            nota = boletin.values()
            otro_dato = input('Desea agregar otro alumno? Escriba si o no y presione enter.\n')
    if otro_dato == 'si':
        return entrada_boletin(otro_dato)
    elif otro_dato == 'no':
        print (promedio(nota))
#main
# Creo un diccionario vacio
boletin = {}
#inicializo la variable otro_dato
otro_dato = 'asd'
entrada_boletin(otro_dato)
if otro_dato == 'si':
    entrada_boletin(otro_dato)
    if otro_dato == 'no':
        print(promedio(nota))
elif otro_dato == 'no':
    print(promedio(nota))

#################################################################################################################################################
- Se requiere ingresar por pantalla materias de la carrera. La materia se compone con: número de 5 cifras de identificación
única, un nombre y un listado de alumnos (con sus notas).
def entrada_boletin(otro_dato):
    nombre = input('ingrese el nombre del alumno. Minimo 5 caracteres\n')
    if len(nombre) > 4:
        nota = input('ingrese la nota del alumno con un valor entre 0 y 10\n')
        nota = int(nota)
        if -1 < nota < 11:
            nota = int(nota)
            boletin[nombre] = nota
            print(boletin)
            otro_dato = input('Desea agregar otro alumno? Escriba si o no y presione enter.\n')
    if otro_dato == 'si':
        return entrada_boletin(otro_dato)
    elif otro_dato == 'no':
        materias.append(boletin)
        print (materias)
materias = []
boletin = {}
otro_dato = 'asd'
numero = input('ingrese el numero de materia. El mismo debera tener 5 digitos.\n')
if  len(numero) == 5:
    materias.append(numero)
    nombre = input('ingrese el nombre de la materia. El mismo debera tener 5 digitos.\n')
    materias.append(nombre)
    entrada_boletin(otro_dato)
    if otro_dato == 'si':
        entrada_boletin(otro_dato)
        if otro_dato == 'no':
            materias.append(boletin)
            print (materias)
    elif otro_dato == 'no':
        materias.append(boletin)
        print (materias)

##################################################################################################################################
- Dada una cadena de texto de 10 a 20 caracteres ingresada por el usuario quedarse con los primeros 3 y los ultimos 5.
def generar_salida(texto_input):
    for i in range (0,3):
        texto_output.append(texto_input[i])
    for i in range((len(texto_input))-5, len(texto_input)):
        texto_output.append(texto_input[i])
    return (texto_output)
texto_input = []
texto_output = []
texto_input = input('Escriba un texto de entre 10 y 20 caracteres.\n')
if 9 < len(texto_input) < 21:
    print(generar_salida(texto_input))
else:
    print ('El texto debe tener entre 10 y 20 caracteres')
###################################################################################################################################################################################################
- Se debera generar un sistema que mantenga en memoria datos de una agenda.
    - El programa mostrara las opciones> agregar, editar, borrar, mostrar y salir
    agregar, agenda un contacto (email, telefono, nombre, domicilio, edad y dni)
    editar, permite modificar cualquiera de los contactos seleccionando su email.
    borrar, elimina un contacto

'''


def agregar(nuevo_contacto):
    nuevo_contacto = input('ingrese el nombre del nuevo contacto\n')
    nuevo_contacto_info = {}
    contactos[nuevo_contacto] = nuevo_contacto_info

    mail = input('ingrese el E-mail del nuevo contacto\n')
    nuevo_contacto_info['E-mail'] = mail

    tel = input('ingrese el telefono del nuevo contacto\n')
    nuevo_contacto_info['Telefono'] = tel

    domicilio = input('ingrese el domicilio del nuevo contacto\n')
    nuevo_contacto_info['Domicilio'] = domicilio

    edad = input('ingrese la edad del nuevo contacto\n')
    nuevo_contacto_info['Edad'] = edad

    dni = input('ingrese el DNI del nuevo contacto\n')
    nuevo_contacto_info['DNI'] = dni


def agenda(texto_inicio):
    nuevo_contacto = 'iniciando'

    texto_inicio = input('Seleccione una de las siguiente opciones.\nagregar, editar ,borrar, mostrar, salir \n  ')

    if texto_inicio == 'agregar':

        agregar(nuevo_contacto)

        print(texto_inicio)
        print(contactos)
        texto_inicio = ' '
        agenda(texto_inicio)

    elif texto_inicio == 'borrar':
        contacto_a_borrar = input('ingrese nombre del contacto a borrar\n')
        del contactos[contacto_a_borrar]

        print(contactos)
        texto_inicio = ' '
        agenda(texto_inicio)

    elif texto_inicio == 'editar':

        contacto_a_editar = input('Seleccione el E-mail contacto a editar\n')

        if contacto_a_editar in contactos:

            editar = contactos[contacto_a_editar]
        else:
            print('El mail no existe.')
            contacto_a_editar = input('Seleccione el E-mail contacto a editar\n')

        agregar(contacto_a_editar)
        texto_inicio = ' '
        agenda(texto_inicio)

    elif texto_inicio == 'salir':

        return (contactos)


opciones = ['agregar', 'editar', 'borrar', 'mostrar', 'salir']

contactos = {}
contacto_particular = {}

texto_inicio = 'inicio'

agenda(texto_inicio)


global1 = 34

def cambiar_global(f):
    '''Cambiar una variable global

    Esta función debe asignarle a la variable global `global1` el valor que se
    le pasa como único argumento posicional.
    '''
    #pass
    global global1
    global1 = f



def anio_bisiesto(anio):
    '''Responder si el entero pasado como argumento es un año bisiesto
    
    Para determinar si un año es bisiesto, se deben tener en cuenta las 
    siguientes condiciones:

    - Si el año es divisible por 4 es bisiesto, a menos que:
        - Si el año es divisible por 100 no es bisiesto a menos que:
            - Si el año es divisible por 400 es bisiesto.

    Retorna True o False
    '''
    
    if anio % 400 == 0 or (anio % 100 !=0 and anio %4 ==0):
      return True
    else:
      return False
    #pass

def contar_valles(a):
    r'''Contar el número de valles

    Esta función debe recibir como argumento una lista de -1's, 0's y 1's, y lo 
    que representan son las subidas y las bajadas en una ruta de caminata. -1
    representa un paso hacia abajo, el 0 representa un paso hacia adelante y el 
    1 representa un paso hacia arriba, entonces por ejemplo, para la lista
    [-1,1,0,1,1,-1,0,0,1,-1,1,1,-1,-1] representa la siguiente ruta:

                /\
         /\__/\/  \
       _/  
     \/

    El objetivo de esta función es devolver el número de valles que estén 
    representados en la lista, que para el ejemplo que se acaba de mostrar es
    de 3 valles.
    '''
    cont = 0
    b = False
    for el in a:
      if el == -1 and b == False:
        b = True
      if el == 1 and b == True:
        b = False
        cont += 1
    return cont
    pass
    #pass

def saltando_rocas(salto):
    '''Mínimo número de saltos en las rocas

    Esta función hace parte de un juego en el que el jugador debe cruzar un río
    saltando de roca en roca hasta llegar al otro lado. Hay dos tipo de rocas, 
    secas y húmedas, y el jugador debe evitar saltar encima de las húmedas para 
    no resbalarse y caer. Además el jugador puede saltar 1 o 2 rocas, siempre y 
    cuando no caiga en una húmeda.

    Esta función debe recibir como argumento una lista de ceros y unos. Los ceros 
    representan las rocas secas y los unos las húmedas.
    El objetivo es devolver el número mínimo de saltos que debe realizar el 
    jugador para ganar la partida
    '''
    saltos = 0
    valor = 0
    while valor < len(salto)-1:
      print(valor)
      if valor < len(salto)-2:
        if salto[valor+2] == 0:
          saltos = saltos +1
          valor = valor +2
        elif salto[valor+1] == 0:
          saltos = saltos +1
          valor = valor +1
      elif valor < len(salto)-1:
        if salto[valor+1] == 0:
          saltos = saltos +1
          valor= valor +1
        else:
          valor = valor +1
    valor = valor +1
    return saltos
    pass

def pares_medias(data):
    '''Contar pares de medias

    Esta función debe recibir como argumento una lista de enteros. Cada elemento
    de esta lista representa el color de una media, y por lo tanto si hay dos 
    elementos que tienen el mismo entero, esas dos medias tienen el mismo color.
    El objetivo de esta función es devolver un diccionario cuyas keys son cada 
    uno de los colores que se encuentren en la lista, y los valores son la 
    cantidad de pares que se han encontrado para cada color.
    '''
    diccionario = {}
    verificarPar = []
    for valor in data:
      diccionario.setdefault(valor,0)
    for el in data:
      diccionario[el] += 1
    for valor2 in diccionario:
      diccionario[valor2] = diccionario[valor2]//2
    for el2 in diccionario:
      if diccionario[el2] == 0:
        verificarPar.append(el2)
    for valor3 in verificarPar:
      del diccionario[valor3]    
    return diccionario
    pass
    #pass

""" Crear una clase llamada `ListaComa` que reciba en su constructor un iterable
# con el valor inicial para una lista que se guardará en un atributo llamado 
# `lista`. Implementar el método __str__ para que devuelva un string con todos
# los elementos del atributo `lista` unidos a través de comas. Ejemplo:
# si `lista` es [1,2,3,4], __str__ debe devolver '1,2,3,4'""" 

class ListaComa:
  def __init__(lista,iterable):
    lista.iterable = iterable
  
  def __str__(valor):
    listaConstructor = []
    for el in valor.iterable:
      listaConstructor.append(str(el))
    retorno = ','.join(listaConstructor)
    return retorno


"""# Crear una clase llamada `Persona` que reciba en su constructor como 1er 
# argumento un iterable con el valor inicial para una lista que se guardará en
# un atributo llamado `nombres` y como 2do argumento un iterable con el valor 
# inicial para una lista que se guardará en un atributo llamado `apellidos`.
# Antes de guardar estos atributos se debe verificar que todos los elementos 
# de estas dos listas deben ser de tipo str y procesar todos los elementos de
# cada una de las dos listas para que su primera letra sea mayúscula y las demás
# minúsculas.
#
# Implementar el método `nombre_completo` para que devuelva un string con todos 
# los elementos de `nombres` concatenados con espacio, y esto a su vez 
# concatenado con todos los elementos de `appelidos` concatenados con espacio.
# Ejemplo:
# si `nombres` es ['Juan', 'David'] y `apellidos` es ['Torres', 'Salazar'],
# el método `nombre completo` debe devolver  'Juan David Torres Salazar'"""
class Persona:
  def __init__(dataInformacion,nombres,apellidos):
    dataInformacion.nombres = []
    dataInformacion.apellidos = [] 
    for dataValor in nombres:
      dataInformacion.nombres.append(str(dataValor).capitalize())
    for dataValor in apellidos:
      dataInformacion.apellidos.append(str(dataValor).capitalize())
  
  def nombre_completo(dataInformacion):
    informacionDataRetorno =  ' '.join(dataInformacion.nombres)+' '+' '.join(dataInformacion.apellidos)
    return informacionDataRetorno




"""# Crear una clase llamada `Persona1` que herede de la clase `Persona`, y que en su
# constructor reciba además de los atributos del padre, una variable tipo 
# `datetime` como 3er argumento para guardar en atributo `fecha_nacimiento`.
#
# Implementar el método `edad` para que devuelva un `int` que represente la edad
# de la persona y que se calcule restando los años entre la fecha actual y 
# el atributo `fecha_nacimiento`.
# Ejemplo:
# si `fecha_nacimiento` es 1985-10-21 y la fecha actual es 2020-10-20, el método
# `edad` debe devover 35."""
from datetime import datetime
class Persona1(Persona):
  def __init__(retornoFecha,nombres,apellidos,fecha_nacimiento):
    super().__init__(nombres,apellidos)
    retornoFecha.fecha_nacimiento = fecha_nacimiento
  
  def edad(dataInfor):
    fechaActual = datetime.today()
    aniosF = (fechaActual.year - dataInfor.fecha_nacimiento.year) -1 #calculo la diferencia en años y resto 1 porque el año actual se ha definido mayor
    if fechaActual.month > dataInfor.fecha_nacimiento.month:
      aniosF = aniosF +1 #Sumo 1 año porque el mes actual ya paso el mes de nacimiento 
    elif fechaActual.month >= dataInfor.fecha_nacimiento.month and fechaActual.day >= dataInfor.fecha_nacimiento.day:
      aniosF = aniosF +1 #Sumo 1 año porque esta mayor al día 
    return int (aniosF)


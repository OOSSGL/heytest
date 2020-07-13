from django.shortcuts import render
from rest_framework.decorators import api_view
from ..serializers import PruebaSerializer
from rest_framework.response import Response


# Created the objetc test
class Prueba(object):
    def __init__(self, name, description, result):
        self.name = name
        self.description = description
        self.result = result


@api_view(['GET'])
def getPassword(request):
    prueba = Prueba(
        name="Derivar Contraseña (Ethical Hacking)",
        description="Un método de seguridad comúnmente utilizado por los bancos es preguntar tres"
            + "caracteres aleatorios de una contraseña. Por ejemplo, si la contraseña es 531278, "
            + "el banco puede preguntar por el 2do, 3er, y 5to, carácter; esperando que el usuario" 
            + " responda con la secuencia 3-1-7.El archivo keylog.txt contiene 50 secuencias "
            + " correctas para una contraseña específica. Dado que cada una de las secuencias "
            + "está en orden de primer carácter a último carácter, ¿Cuál es la contraseña más "
            + " corta para la cual todas las secuencias son correctas?",
        result="To be discovered")

    prueba.result = "La contraseña es: " + decipherPassword()

    serializer = PruebaSerializer(prueba)
    return Response(serializer.data)


# Decifra el password con el keylog dado
def decipherPassword():

    # Leemos el archivo y los pasamos a un array
    array = []
    with open('keylog.txt') as f:
        for line in f:
            array.append(line[0:3])

    # Normal array used, the index of the array will be the weight, and is sorted by 
    # swapping the two numbers each time they are in the wrong position
    digis = []

    # Get all the digits used
    for i in array:
        for j in i:
            if (j not in digis):
                digis.append(j)

    print(digis)

    # It seems that with only one iteration it works fine
    for i in array:
        # Compare the digits and put the digits in the correct order
        if(digis.index(i[0]) > digis.index(i[1])):
            digis[digis.index(i[0])] = i[1]
            digis[digis.index(i[1])] = i[0]

        if(digis.index(i[1]) > digis.index(i[2])):
            digis[digis.index(i[1])] = i[2]
            digis[digis.index(i[2])] = i[1]

        # print(i[0], digis.index(i[0]))
    print(digis)

    # wow it worked af first try! =D Normally you have to do this swaping a lot 
    # of times but the size of 50 samples was good enough, nice! I made it! =D
    # This one was a LOT easier than the fibonacci one

    password = ""
    for i in digis:
        password += i

    return password

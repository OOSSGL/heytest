from django.shortcuts import render
from rest_framework.decorators import api_view
from .serializers import PruebaSerializer
from rest_framework.response import Response


# Created the objetc test
class Prueba(object):
    def __init__(self, name, description, result):
        self.name = name
        self.description = description
        self.result = result


@api_view(['GET'])
def getAnswer(request):
    prueba = Prueba(
        name="Prueba",
        description="Esto es una prueba para ver si funciona",
        result="IT WORKS!")
    serializer = PruebaSerializer(prueba)
    return Response(serializer.data)


@api_view(['GET'])
def getDomingos(request):
    prueba = Prueba(
        name="¿Cuántos Domingos?",
        description="¿Durante el siglo 20 (1 de enero de 1901 hasta 31 de diciembre de "
            + "2000), cuántos meses han empezado un domingo?",
        result="To be discovered")
    serializer = PruebaSerializer(prueba)
    return Response(serializer.data)


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
    serializer = PruebaSerializer(prueba)
    return Response(serializer.data)


@api_view(['GET'])
def getFibopan(request):
    prueba = Prueba(
        name="Números de Fibonacci Pan-digitales",
        description="F(k) es el primer número de Fibonacci donde los primeros 9 dígitos "
            + "son una secuencia pan-digital y donde los últimos 9 dígitos también son una "
            + "secuencia pan-digital.¿Cuánto es K?",
        result="To be discovered")
    serializer = PruebaSerializer(prueba)
    return Response(serializer.data)


@api_view(['GET'])
def getPascals(request):
    prueba = Prueba(
        name="Triángulo de Pascal",
        description="¿En el triángulo de Pascal cuántas entradas de las primeras mil "
            + "millones de filas (10^9) no son divisibles por 7?",
        result="To be discovered")
    serializer = PruebaSerializer(prueba)
    return Response(serializer.data)

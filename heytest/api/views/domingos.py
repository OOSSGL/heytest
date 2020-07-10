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

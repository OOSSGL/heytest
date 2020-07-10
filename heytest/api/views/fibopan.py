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
def getFibopan(request):
    prueba = Prueba(
        name="Números de Fibonacci Pan-digitales",
        description="F(k) es el primer número de Fibonacci donde los primeros 9 dígitos "
            + "son una secuencia pan-digital y donde los últimos 9 dígitos también son una "
            + "secuencia pan-digital.¿Cuánto es K?",
        result="To be discovered")
    serializer = PruebaSerializer(prueba)
    return Response(serializer.data)

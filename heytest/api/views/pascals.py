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
def getPascals(request):
    prueba = Prueba(
        name="Triángulo de Pascal",
        description="¿En el triángulo de Pascal cuántas entradas de las primeras mil "
            + "millones de filas (10^9) no son divisibles por 7?",
        result="To be discovered")
    serializer = PruebaSerializer(prueba)
    return Response(serializer.data)

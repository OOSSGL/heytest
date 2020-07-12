from django.shortcuts import render
from rest_framework.decorators import api_view
from ..serializers import PruebaSerializer
from rest_framework.response import Response
import math


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
            + "secuencia pan-digital. ¿Cuánto es K?. En la consola del servidor se "
            + "puede ver el número de fibonacci completo, la iteración, la longitud y las "
            + "dos secuencias pan-digital del inicio y del final",
        result="To be discovered")

    prueba.result = "K = " + str(goldenRatio(1000000))

    serializer = PruebaSerializer(prueba)
    return Response(serializer.data)


# Using Golden ratio - IT WORKS! Founded! K is 329468!!!
def goldenRatio(n):
    golden_ratio = (1 + math.sqrt(5))/2
    start = 2
    m = 1
    l = 1
    for i in range(3, n):
        # Normal iteration of fibonacci
        h = m
        m = m + l
        l = h

        # start =  only the first numbers, we multiply it with the golden ratio to get an 
        # aproximation of the fibonacci number each iteration
        start = int(start * golden_ratio)

        # have to make it maximun 30 digits or else we will get overflow to infinite
        if(start>1E30):
            start = int(start*1E-3)
        
        # First we check if the first numbers are pandigital
        if(isPandigital(set(str(start)[0:9]))):
            #print("\nSTART", i, len(str(m)), m, sep=": ")
            #print("START", str(start)[0:9])
            
            # Second we check if the last numbers are pandigital, if they are we founded 
            # the number!
            if(isPandigital(set(str(m)[-9:]))):
                print("\nFINISH AND FINISH\nIteration  |  # of Digits  |  Full number\n", 
                    i, len(str(m)), m, sep=": ")
                print("START", str(start)[0:9], "FINISH", str(m)[-9:])
                return i


# Check if it is pandigital with sets simpler
def isPandigital(number):
    if(number == set("123456789")):
        return True

from rest_framework import serializers


class PruebaSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=250)
    description = serializers.CharField(max_length=1000)
    result = serializers.CharField(max_length=250)

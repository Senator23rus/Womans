import io


from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from .models import Women

from rest_framework import serializers

class WomenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Women
        fields = ('__all__')


# class WomenModel:
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# def encode():
#     model = WomenModel('Agelina Jolie', 'Content: Agelina Jolie')
#     model_sr = WomenSerializer(model)
#     print(model_sr.data, type(model_sr.data), sep='\n')
#     json = JSONRenderer().render(model_sr.data)
#     print(json)
#
# def decode():
#     stream = io.BytesIO(b'{"title":"Agelina Jolie","content":"Content: Agelina Jolie"}')
#     data = JSONParser().parse(stream)
#     serializer = WomenSerializer(data=data)
#     serializer.is_valid()
#     print(serializer.validated_data)
from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import CitySerializer, StateSerializer, CountrySerializer
from .models import City, State, Country

class CityViewset(viewsets.ViewSet):
    def create(self, request):
        try:
            serializer = CitySerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as e:
            return Response({"msg":str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
class CountryDetailViewset(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    serializer_class = CountrySerializer
    lookup_field = 'slug'  # Set the lookup field to 'slug'


        

from rest_framework import serializers 
from .models import Country, State, City 

class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City 
        fields = '__all__'
        
class CityDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = City 
        fields = ['id', 'name', 'slug']
         
class StateSerializer(serializers.ModelSerializer):
    cities = CityDetailSerializer(many=True, read_only=True)
    class Meta:
        model = State 
        fields = ['id', 'name', 'slug', 'cities']
        
class CountrySerializer(serializers.ModelSerializer):
    states = StateSerializer(many=True, read_only=True)
    class Meta:
        model = Country 
        fields = ['id', 'name', 'code', 'slug', 'states']
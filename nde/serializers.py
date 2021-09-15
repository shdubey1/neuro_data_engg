# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import GeeksModel, Hero

# Create a model serializer
class GeeksSerializer(serializers.HyperlinkedModelSerializer):
	# specify model and fields
	class Meta:
		model = GeeksModel
		fields = ('csrfmiddlewaretoken','title', 'description')

class HeroSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Hero
		fields = ('name', 'alias')

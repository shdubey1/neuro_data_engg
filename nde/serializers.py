# import serializer from rest_framework
from rest_framework import serializers

# import model from models.py
from .models import  EDAJSON, GeeksModel, Hero, EDA, MissingValues, Correlation, MissingValuesPlotting, SampleOfFirstNLastRows,  Graph

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

class EDASerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = EDA
		fields = ('missing_vals', 'correlation', 'missing_vals_plotting', 'sample_of_first_n_last_rows', 'graphs')

class MissingValuesSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MissingValues
		fields = ('missing_vals', 'mean', 'median', 'mode', 'memory_size')

class CorrelationSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Correlation
		fields = ('title', 'correlation_graph')

class MissingValuesPlottingSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = MissingValuesPlotting
		fields = ('title', 'missing_vals_plotting')

class SampleOfFirstNLastRowsSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = SampleOfFirstNLastRows
		fields = ('first_rows', 'last_rows')

class GraphSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = Graph
		fields = ('first_rows', 'last_rows')


class EDAJSONSerializer(serializers.HyperlinkedModelSerializer):
	class Meta:
		model = EDAJSON
		fields = ('missing_vals', 'correlation', 'missing_vals_plotting', 'sample_of_first_n_last_rows', 'graphs')
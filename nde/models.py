from django.db import models

class MissingValues(models.Model):
	missing_vals = models.IntegerField(null=True)
	mean = models.DecimalField(null=True, max_digits=20, decimal_places = 2)
	median = models.DecimalField(null=True, max_digits=20, decimal_places = 2)
	mode = models.DecimalField(null=True, max_digits=20, decimal_places = 2)
	memory_size = models.DecimalField(null=True, max_digits=20, decimal_places = 2)

class Correlation(models.Model):
	title = models.CharField(max_length=10)
	correlation_graph = models.ImageField()


class MissingValuesPlotting(models.Model):
	title = models.CharField(max_length=50)
	missing_vals_plotting = models.ImageField()
	

class SampleOfFirstNLastRows(models.Model):
	first_rows = models.IntegerField()
	last_rows = models.IntegerField()

class Graph(models.Model):
	title = models.CharField(max_length=50)
	graph = models.ImageField()
	

class EDA(models.Model):
	missing_vals = models.ForeignKey(MissingValues, on_delete= models.SET_NULL, null=True)
	correlation = models.ForeignKey(Correlation, on_delete= models.SET_NULL, null=True)
	missing_vals_plotting = models.ForeignKey(MissingValuesPlotting, on_delete= models.SET_NULL, null=True)
	sample_of_first_n_last_rows = models.ForeignKey(SampleOfFirstNLastRows, on_delete= models.SET_NULL, null=True)
	graphs = models.ForeignKey(Graph, on_delete= models.SET_NULL, null=True)

	def __str__(self):
		return self.name
		
class EDAJSON(models.Model):
	missing_vals = models.CharField(max_length=10000)
	correlation = models.CharField(max_length=10000)
	missing_vals_plotting = models.CharField(max_length=10000)
	sample_of_first_n_last_rows = models.CharField(max_length=10000)
	graphs = models.CharField(max_length=10000)

	def __str__(self):
		return self.name
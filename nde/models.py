from django.db import models

class Hero(models.Model):
	name = models.CharField(max_length=60)
	alias = models.CharField(max_length=60)
	def __str__(self):
		return self.name


class GeeksModel(models.Model):
	csrfmiddlewaretoken = models.CharField(max_length = 1000)
	title = models.CharField(max_length = 200)
	description = models.TextField()


	def __str__(self):
		return self.title



# from django.db import models

# # Create your models here.

# import uuid
# from cassandra.cqlengine import columns
# from cassandra.cqlengine.models import Model
 
# class ExampleModel(Model):
#     read_repair_chance = 0.05 # optional - defaults to 0.1
#     example_id = columns.UUID(primary_key=True, default=uuid.uuid4)
#     description = columns.Text(required=False)
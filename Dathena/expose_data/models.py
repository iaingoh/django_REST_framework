from django.db import models

class JsonDataPoint(models.Model):
    name = models.CharField(max_length=10)
    total_docs = models.IntegerField()

    def __str__(self):
        return self.name
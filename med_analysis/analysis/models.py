from django.db import models
from django.views.generic import FormView
from django.urls import reverse_lazy
from django.http import HttpResponseRedirect
from .forms import MyLoginForm

class Lab(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class MeasurementUnit(models.Model):
    name = models.CharField(max_length=50)
    abbreviation = models.CharField(max_length=10)
    
    def __str__(self):
        return self.name

class Analysis(models.Model):
    name = models.CharField(max_length=50)
    lab = models.ForeignKey(Lab, on_delete=models.CASCADE)
    measurement_unit = models.ForeignKey(MeasurementUnit, on_delete=models.CASCADE)
   # slug = models.SlugField(unique=True, max_length=100, blank=True)

   # def save(self, *args, **kwargs):
    #    if not self.pk:
   #         self.slug = slugify(self.name)
   #     super().save(*args, **kwargs)
    
    def __str__(self):
        return self.name

  #  def get_absolute_url(self):
   #     return reverse('analysis_detail', args=[self.slug])


class AnalysisResult(models.Model):
    analysis = models.ForeignKey(Analysis, on_delete=models.CASCADE)
    value = models.FloatField()
    date = models.DateField()
    lower_limit = models.FloatField()
    upper_limit = models.FloatField()
    
    def __str__(self):
        return f"{self.analysis} - {self.date}"


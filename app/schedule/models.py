# from django.db import models
# from django.urls import reverse

# class Schedule(models.Model):
#     name        = models.CharField(max_length=100)
#     icon        = models.ImageField(upload_to='media/')
#     price       = models.IntegerField()

#     def __str__(self):
#         return self.name

#     def get_absolute_url(self):
#         return reverse('equipment:equipment_update', kwargs={'pk': self.pk})

from django.db import models

# Create your models here.


class Blog(models.Model):
   
    title = models.CharField(max_length=250, null=False, blank=False)
    body = models.TextField(null=False, blank=False)
    image = models.ImageField(null=True, blank=True)
    date_added = models.DateTimeField(null=False, blank=False, auto_now_add=True)

    def __str__(self):
        return self.title

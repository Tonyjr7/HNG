from django.db import models

# Create your models here.
class ME(models.Model):
    email = models.EmailField()
    github_url = models.URLField()

    def __str__(self):
        return self.email 

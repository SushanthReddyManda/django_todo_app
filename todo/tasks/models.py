from django.db import models

# Create your models here.
class model_class(models.Model):
    create = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=200)
    complete  = models.BooleanField(default=False)

    def __str__(self):
        return self.title

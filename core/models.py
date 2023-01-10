from django.db import models

# Create your models here.
class WaitlistUser(models.Model):
    email = models.EmailField(null=False, unique=True)

    def __str__(self):
        return f"{self.email}"
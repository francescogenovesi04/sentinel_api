from django.db import models

class TargetAPI(models.Model):
    name = models.CharField(max_length=100)
    swagger_url = models.URLField()
    last_content = models.TextField(null=True, blank=True)
    last_analysis = models.TextField(null=True, blank=True) # <--- Nuovo campo
    last_status = models.IntegerField(null=True, blank=True)
    last_check = models.DateTimeField(auto_now=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name
from django.db import models

# Create your models here.
from django.db import models
import uuid

class ScrapingTask(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    coins = models.TextField()
    status = models.CharField(max_length=50, default='PENDING')
    result = models.JSONField(null=True, blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.id)

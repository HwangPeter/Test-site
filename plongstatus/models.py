from django.db import models
from datetime import datetime
# Create your models here.
class Status(models.Model):
    """
    Model representing the current status of Plong Bot's session cookie.
    """
    status = models.CharField(max_length=100, help_text="Enter the current status.")
    timestamp = models.CharField(max_length=50, default=datetime.now(), help_text="Timestamp of last update.", editable=False)

    def __str__(self):
        """
        String for representing the Model object
        """
        return self.status

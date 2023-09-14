from django.db import models
from django.db.models.signals import pre_delete
from django.dispatch import receiver
import os

from .models import Teacher

@receiver(pre_delete, sender=Teacher)
def delete_media_file(sender, instance, **kwargs):
    # Check if the instance has a file field (e.g., 'photo')
    if hasattr(instance, 'photo') and instance.photo:
        # Get the file path
        file_path = instance.photo.path

        # Check if the file exists
        if os.path.exists(file_path):
            # Delete the file from the media folder
            os.remove(file_path)

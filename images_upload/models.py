from django.conf import settings
from django.core.files.storage import FileSystemStorage
from django.db import models
from django.urls import reverse
from thumbnails.fields import ImageField


class Image(models.Model):
    title = models.CharField(max_length=50)
    url = models.URLField(max_length=2000, blank=True)
    image = ImageField(storage=FileSystemStorage(), upload_to='images/')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created_at']),
        ]
        ordering = ['-created_at']

    def thumbnail_small_url(self):
        return self.image.thumbnails.small.url

    def thumbnail_large_url(self):
        return self.image.thumbnails.large.url

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': str(self.pk)})


from django.conf import settings
from django.db import models
from django.urls import reverse


class Image(models.Model):
    title = models.CharField(max_length=50)
    img = models.ImageField(upload_to='images/',  blank=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('image_detail', kwargs={'pk': str(self.pk)})

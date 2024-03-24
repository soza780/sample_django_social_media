from django.db import models
from django.contrib.auth import get_user_model
from django.utils.text import slugify


# Create your models here.

class Image(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name='images_created')
    title = models.CharField(max_length=250)
    slug = models.SlugField(max_length=250, unique=True)
    url = models.URLField(max_length=2000)
    image = models.ImageField(upload_to='images/%Y/%m/%d/')
    description = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        indexes = [
            models.Index(fields=['-created']),
        ]
        ordering = ['-created']

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    video_file = models.FileField(upload_to='videos/')
    
    def __str__(self):
        return self.title
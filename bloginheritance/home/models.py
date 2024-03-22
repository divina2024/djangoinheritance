from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=200)
    body = models.TextField()
    link_url = models.URLField()
    image = models.ImageField(upload_to='article_images/')
    date = models.DateField(auto_now_add=True) 

    def __str__(self):
        return self.title

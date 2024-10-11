from django.db import models

class Bookmark(models.Model):
    title = models.CharField(max_length=200, default="Untitled")  # Title
    url = models.URLField()  # URL

    def __str__(self):
        return self.title

from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.TextField(())
    upload_image = models.ImageField(upload_to='images/')

    def __str__(self):
        """
        :return:
        """
        return self.title

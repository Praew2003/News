from django.db import models

prefix_choices = (
    (1, "นาย"),
    (2, "นางสาว"),
    (3, "นาง"),
)


class News(models.Model):

    name = models.CharField(max_length=255)
    content = models.TextField()

    class Meta:
        verbose_name = "News"
        verbose_name_plural = "News"

    def __str__(self):
        return self.name

    
class Writer(models.Model):
    
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
  

    class Meta:
        verbose_name = "Writer"
        verbose_name_plural = "Writer"

    def __str__(self):
        return self.name


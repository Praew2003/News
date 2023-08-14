from django.db import models

class Writer(models.Model):
    
    name = models.CharField(max_length=255)
    lastname = models.CharField(max_length=255)
    
    def __str__(self):
        return f"{self.name} {self.lastname}"
    
class News(models.Model):

    title = models.CharField(max_length=255)
    detail = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    by = models.ForeignKey(Writer, on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.title}, {self.by}"    


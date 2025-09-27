from django.db import models

# Create your models here.
# Author model represents book authors
class  Author(models.Model):
  name = models.CharField(max_length=100)
  def __str__(self):
    return self.name
  
# Book model stores books and links to Author
  
class Book(models.Model):
  title = models.TextField()
  publication_year = models.IntegerField()
  author = models.ForeignKey(Author,on_delete=models.CASCADE, related_name= "books")

  def __str__(self):
    return self.title
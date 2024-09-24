from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)
    surname = models.CharField(max_length=255)
    bio = models.TextField()

    def __str__(self):
        return f"{self.name} {self.surname}"

class News(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    date_of_publication = models.DateField()
    full_text_of_material = models.TextField()

    def __str__(self):
        return self.title
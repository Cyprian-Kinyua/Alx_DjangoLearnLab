from django.db import models

# Create your models here.
# The Author model stores ingormation about book authors.


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# The book model stores information about books.
# Each book is linked to an author via a foreign key (one-to-many relationship) relationship.


class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(
        Author, related_name='books',  # allows reverse lookup: author.books.all()
        on_delete=models.CASCADE)

    def __str__(self):
        return self.title

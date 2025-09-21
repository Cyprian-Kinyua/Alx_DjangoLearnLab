from relationship_app import models

books_by_author = models.Book.objects.filter(author__name='J.K. Rowling')

books = models.Library.objects.get(name='library_name').books.all()

librarian = models.Librarian.objects.get(
    models.Library.objects.get(name='Central Library').librarian.id)

from relationship_app.models import Author, Book, Library, Librarian

author_name = 'J.K. Rowling'
author = Author.objects.get(name=author_name)
books_by_author = author.objects.filter(author=author)

library_name = "Nairobi Library"
books = Library.objects.get(name=library_name).books.all()

librarian = Librarian.objects.get(
    Library.objects.get(name='Central Library').librarian.id)

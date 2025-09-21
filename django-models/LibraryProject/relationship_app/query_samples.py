from relationship_app.models import Author, Book, Library, Librarian

books_by_author = Book.objects.filter(author__name='J.K. Rowling')

library_name = "Nairobi Library"
books = Library.objects.get(name=library_name).books.all()

librarian = Librarian.objects.get(
    Library.objects.get(name='Central Library').librarian.id)

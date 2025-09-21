from bookshelf.models import Book
book=Book.objects.get(title="NineteenEighty-Four")
book.delete()
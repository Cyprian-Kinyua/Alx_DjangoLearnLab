from bookshelf.models import Book
book1=Book.objects.get(title="NineteenEighty-Four")
book1.delete()
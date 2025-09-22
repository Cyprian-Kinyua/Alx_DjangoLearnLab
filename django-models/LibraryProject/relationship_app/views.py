from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth import login
from .models import Book
from .models import Library
from django.views.generic.detail import DetailView
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.decorators import permission_required

# Create your views here.


def list_books(request):
    books = Book.objects.select_related('author').all()
    return render(request, 'relationship_app/list_books.html', 'Book.objects.all()')


class LibraryDetailView(DetailView):
    model = Library
    template_name = 'relationship_app/library_detail.html'
    context_object_name = 'library'


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('list_books')
    else:
        form = UserCreationForm()
    return render(request, 'relationship_app/register.html', {'form': form})


@permission_required('relationship_app.can_add_book', raise_exception=True)
def add_book(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        published_date = request.POST.get('published_date')

        Book.objects.create(title=title, author=author,
                            published_date=published_date)
        return redirect('book_list')
    return render(request, 'books/add_book.html')


@permission_required('relationship_app.can_change_book', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.published_date = request.POST.get('published_date')
        book.save()
        return redirect('book_list')
    return render(request, 'books/edit_book.html', {'book': book})


@permission_required('relationship_app.can_delete_book', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, id=book_id)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})


class LoginView(LoginView):
    template_name = 'relationship_app/login.html'


class LogoutView(LogoutView):
    template_name = 'relationship_app/logout.html'


def is_admin(user):
    return hasattr(user, 'profile') and user.profile.role == 'Admin'


def is_librarian(user):
    return hasattr(user, 'profile') and user.profile.role == 'Librarian'


def is_member(user):
    return hasattr(user, 'profile') and user.profile.role == 'Member'


@user_passes_test(is_admin)
def admin_view(request):
    return render(request, 'relationship_app/admin_view.html')


@user_passes_test(is_librarian)
def librarian_view(request):
    return render(request, 'relationship_app/librarian_view.html')


@user_passes_test(is_member)
def member_view(request):
    return render(request, 'relationship_app/member_view.html')

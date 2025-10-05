from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Book, Author
from django.contrib.auth.models import User

"""
This module tests all API endpoints for the book model:
 - A built-in API client to simulate real HTTP requests.
 - Automatic test database setup and teardown.
"""


class BookAPITestCase(APITestCase):
    """Comprehensive test case for Book CRUD operations, filtering, search, and permissions."""

    def setUp(self):
        """Set up data and authentication for each test."""
        # Create a test user
        self.user = User.objects.create_user(
            username='testuser', password='password123')

        # Create an author
        self.author = Author.objects.create(name="John Doe")

        # Create sample books
        self.book1 = Book.objects.create(
            title="Learning Django",
            publication_year=2021,
            author=self.author
        )
        self.book2 = Book.objects.create(
            title="Mastering Python",
            publication_year=2020,
            author=self.author
        )

        # URLs for endpoints
        self.list_url = reverse('book-list')  # /api/books/
        self.detail_url = reverse(
            'book-detail', args=[self.book1.id])  # /api/books/1/

    # ------------------------------------------------------------------------
    # TEST 1: LIST ALL BOOKS
    # ------------------------------------------------------------------------
    def test_list_books(self):
        """Ensure the list endpoint returns all books."""
        response = self.client.get(self.list_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 2)  # Should return both books

    # ------------------------------------------------------------------------
    # TEST 2: RETRIEVE A SINGLE BOOK
    # ------------------------------------------------------------------------
    def test_get_single_book(self):
        """Ensure we can retrieve a single book by ID."""
        response = self.client.get(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], self.book1.title)

    # ------------------------------------------------------------------------
    # TEST 3: CREATE A BOOK (Authenticated)
    # ------------------------------------------------------------------------
    def test_create_book_authenticated(self):
        """Ensure authenticated users can create a book."""
        self.client.login(username='testuser',
                          password='password123')  # simulate login
        data = {
            'title': 'Django Advanced',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 3)

    # ------------------------------------------------------------------------
    # TEST 4: CREATE A BOOK (Unauthenticated)
    # ------------------------------------------------------------------------
    def test_create_book_unauthenticated(self):
        """Ensure unauthenticated users cannot create books."""
        data = {
            'title': 'Unauthorized Book',
            'publication_year': 2024,
            'author': self.author.id
        }
        response = self.client.post(self.list_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    # ------------------------------------------------------------------------
    # TEST 5: UPDATE BOOK
    # ------------------------------------------------------------------------
    def test_update_book(self):
        """Ensure authenticated users can update a book."""
        self.client.login(username='testuser', password='password123')
        data = {'title': 'Updated Title',
                'publication_year': 2021, 'author': self.author.id}
        response = self.client.put(self.detail_url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    # ------------------------------------------------------------------------
    # TEST 6: DELETE BOOK
    # ------------------------------------------------------------------------
    def test_delete_book(self):
        """Ensure authenticated users can delete a book."""
        self.client.login(username='testuser', password='password123')
        response = self.client.delete(self.detail_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Book.objects.filter(id=self.book1.id).exists())

    # ------------------------------------------------------------------------
    # TEST 7: FILTERING
    # ------------------------------------------------------------------------
    def test_filter_books_by_publication_year(self):
        """Ensure filtering by publication_year works."""
        response = self.client.get(f"{self.list_url}?publication_year=2021")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Learning Django')

    # ------------------------------------------------------------------------
    # TEST 8: SEARCH
    # ------------------------------------------------------------------------
    def test_search_books_by_title(self):
        """Ensure search functionality works."""
        response = self.client.get(f"{self.list_url}?search=Python")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Mastering Python')

    # ------------------------------------------------------------------------
    # TEST 9: ORDERING
    # ------------------------------------------------------------------------
    def test_order_books_by_publication_year(self):
        """Ensure ordering by publication year works."""
        response = self.client.get(
            f"{self.list_url}?ordering=publication_year")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data[0]['title'],
                         'Mastering Python')  # Oldest first

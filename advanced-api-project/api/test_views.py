from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    """
    This test case uses a separate test database.
    """

    @classmethod
    def setUpTestData(cls):
        # Create a test user (used for all tests)
        cls.user = User.objects.create_user(username="testuser", password="testpass")

        # Create an author and a book (used for all tests)
        cls.author = Author.objects.create(name="Haddis Alemayehu")
        cls.book = Book.objects.create(
            title="Fikir Eske Mekabir",
            publication_year=1968,
            author=cls.author
        )

    def setUp(self):
        # Log in the test client before each test
        self.client.login(username="testuser", password="testpass")

    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check that the response contains the book we created
        self.assertTrue(any(book["title"] == "Fikir Eske Mekabir" for book in response.data))

    def test_create_book(self):
        url = reverse("book-list")
        data = {
            "title": "Oromay",
            "publication_year": 1983,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        # Check that the response data matches what we sent
        self.assertEqual(response.data["title"], "Oromay")
        self.assertEqual(response.data["publication_year"], 1983)
        self.assertEqual(response.data["author"], self.author.id)

    def test_update_book(self):
        url = reverse("book-detail", args=[self.book.id])
        data = {
            "title": "Fikir Eske Mekabir (Updated)",
            "publication_year": 1968,
            "author": self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Verify the book title was updated
        self.assertEqual(response.data["title"], "Fikir Eske Mekabir (Updated)")

    def test_delete_book(self):
        url = reverse("book-detail", args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        # Verify the book no longer exists
        self.assertFalse(Book.objects.filter(id=self.book.id).exists())

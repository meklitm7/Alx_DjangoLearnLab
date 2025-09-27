from django.urls import reverse
from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create_user(username="testuser", password="testpass")
        
        # Log in the test client
        self.client.login(username="testuser", password="testpass")

        # Create an author and a book
        self.author = Author.objects.create(name="Haddis Alemayehu")
        self.book = Book.objects.create(
            title="Fikir Eske Mekabir",
            publication_year=1968,
            author=self.author
        )

    def test_list_books(self):
        url = reverse("book-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_create_book(self):
        url = reverse("book-list")
        data = {
            "title": "Oromay",
            "publication_year": 1983,
            "author": self.author.id
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_update_book(self):
        url = reverse("book-detail", args=[self.book.id])
        data = {
            "title": "Fikir Eske Mekabir (Updated)",
            "publication_year": 1968,
            "author": self.author.id
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_delete_book(self):
        url = reverse("book-detail", args=[self.book.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

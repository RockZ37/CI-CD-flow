from django.test import TestCase
from .models import Todo

class TodoModelTests(TestCase):
    def test_create_todo(self):

        todo = Todo.objects.create(title="Learn CI/CD", completed=False)

        retrieved = Todo.objects.get(title="Learn CI/CD")

        self.assertEqual(retrieved.title, "Learn CI/CD")
        self.assertFalse(retrieved.completed)

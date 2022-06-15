from django.test import TestCase
from .models import Item


class TestViews(TestCase):
    def test_get_todo_list(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/todo_list.html")

    def test_get_add_item_page(self):
        response = self.client.get("/add")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/add_item.html")

    def test_get_edit_item_page(self):
        item = Item.objects.create(name="Test Get Edit Item Page")
        response = self.client.get(f"/edit/{item.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "todo/edit_item.html")

    def test_add_item(self):
        response = self.client.post("/add", {"name": "Test Add Item"})
        self.assertRedirects(response, "/")

        # Ensure the newly created object is retrievable otherwise fail
        #
        # This is not required as the assertRedirects test would fail before
        # this, but remains as an example.
        try:
            Item.objects.get(name="Test Add Item")
        except Item.DoesNotExist as e:
            self.fail(e)

    def test_delete_item(self):
        item = Item.objects.create(name="Test Delete Item")
        response = self.client.get(f"/delete/{item.id}")
        self.assertRedirects(response, "/")

        # Additional test to ensure the item is not in the database using
        # filter
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

        # Alternate test to ensure the item is not in the database using get
        with self.assertRaises(Item.DoesNotExist):
            Item.objects.get(id=item.id)

    def test_toggle_item(self):
        item = Item.objects.create(name="Test Toggle Item", done=True)
        response = self.client.get(f"/toggle/{item.id}")
        self.assertRedirects(response, "/")
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)

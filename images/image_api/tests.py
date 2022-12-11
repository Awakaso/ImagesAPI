import json

from django.test import TestCase
from .models import Image
from rest_framework.test import APIRequestFactory
from .views import image, image_create
from django.core.exceptions import ObjectDoesNotExist

# Create your tests here.

# GET test
class GetImageTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.image = Image.objects.create(title="test_999", image_url="https://www.google.pt/", description="test_999")

    def test_get_image(self):
        # Create an instance of a GET request using a specific id (created above)
        request = self.factory.get(f'/images/{self.image.id}')

        # Test image() as if it were deployed at /images/<int:pk>
        response = image(request, pk=self.image.id)
        self.assertEqual(response.status_code, 200)  # test GET
        response.render()
        content = json.loads(response.content)  # serialize complex data to json data
        self.assertEqual(content["id"], self.image.id)  # confirm if returned id is equal to created id above

    def tearDown(self) -> None:
         Image.objects.filter(id=self.image.id).delete()


# POST test
class PostImageTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()

    def test_post_image(self):
        # Create an instance of a POST request using a specific id (created above)
        request = self.factory.post('/images/create/', {"title": "test_999", "image_url": "https://www.google.pt/", "description": "test_999"})

        # Test image_create() as if it were deployed at /images/create/
        response = image_create(request)
        self.assertEqual(response.status_code, 200)  # test POST
        response.render()
        self.content = json.loads(response.content)  # serialize complex data to json data
        image = Image.objects.get(id=self.content["id"])  # get instance from db
        self.assertIsNotNone(image)  # return if image is None

    def tearDown(self) -> None:
         Image.objects.filter(id=self.content["id"]).delete()


# PUT test
class PutImageTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.image = Image.objects.create(title="test_999", image_url="https://www.google.pt/", description="test_999")

    def test_put_image(self):
        # Create an instance of a PUT request using a specific id (created above)
        request = self.factory.put(f'/images/{self.image.id}', {"title": "new_test_999", "image_url": self.image.image_url, "description": self.image.description})

        # Test image() as if it were deployed at /images/<int:pk>
        response = image(request, pk=self.image.id)
        self.assertEqual(response.status_code, 200)  # test PUT
        response.render()
        self.image.refresh_from_db()  # refresh value from db after update
        content = json.loads(response.content)  # serialize complex data to json data
        self.assertEqual(content["title"], self.image.title)  # confirm if returned title is different to title above

    def tearDown(self) -> None:
         Image.objects.filter(id=self.image.id).delete()


# DELETE test
class DeleteImageTest(TestCase):
    def setUp(self):
        self.factory = APIRequestFactory()
        self.image = Image.objects.create(title="test_999", image_url="https://www.google.pt/", description="test_999")

    def test_delete_image(self):
        # Create an instance of a DELETE request using a specific id (created above)
        request = self.factory.delete(f'/images/{self.image.id}')

        # Test image() as if it were deployed at /images/<int:pk>
        response = image(request, pk=self.image.id)
        self.assertEqual(response.status_code, 204)  # test DELETE

        # Image.objects.get(id=self.image.id)  # get instance from db
        self.assertRaises(ObjectDoesNotExist, Image.objects.get, id=self.image.id)  # return if image is None




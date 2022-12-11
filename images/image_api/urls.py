from django.urls import path
from image_api.views import image_list, image_create, image

urlpatterns = [
    path('images/create/', image_create),
    path('images/', image_list),
    path('images/<int:pk>', image)
]
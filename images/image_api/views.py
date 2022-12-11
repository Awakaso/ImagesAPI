from image_api.models import Image
from image_api.serializer import ImageSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view


# Create your views here.

# Get reg from db
@api_view(['GET'])
def image_list(request):
    # Process to parse the data // Parsing automaticaly to Json
    images_cd = Image.objects.all()                     # images_cd - Complex data
    serializer = ImageSerializer(images_cd, many=True)  # serializer - Json/Dict data format
    return Response(serializer.data)


# Create reg on db
@api_view(['POST'])
def image_create(request):
    # Process to parse the data // Parsing automaticaly to Complex data
    serializer = ImageSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    else:
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Actions for a single register
@api_view(['GET', 'PUT', 'DELETE'])
def image(request, pk):
    # Try to get reg with pk from db
    try:
        images_cd = Image.objects.get(pk=pk)
    except:
        return Response({
            'error': 'Image does not exist'
        }, status=status.HTTP_404_NOT_FOUND)

    # Show the returned reg from db
    if request.method == 'GET':
        serializer = ImageSerializer(images_cd)
        return Response(serializer.data)

    # Update reg on db
    if request.method == 'PUT':
        serializer = ImageSerializer(images_cd, data=request.data)  # passing instance and data
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    # Delete reg from db
    if request.method == 'DELETE':
        images_cd.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

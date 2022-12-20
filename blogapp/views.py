from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.db.models import F

from .serializers import BlogPostSirializer


# Create your views here.
class CreateBlog(APIView):

    def post(self, request, *args, **kwargs):
        return Response({'message': 'OK'}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        post = BlogPost.objects.all().values()
        print("post",list(post))
        # serializer = BlogPostSirializer(post, many=True)
        # print("serializer", serializer)
        return Response({"data": list(post)}, status=status.HTTP_200_OK)

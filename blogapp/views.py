from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from django.http import HttpResponse

from django.db.models import F

from .serializers import BlogPostSirializer


# Create your views here.
class CreateBlog(APIView):

    def post(self, request, *args, **kwargs):
        print("Request Body:", request.data)
        print("Request args:", args)
        print("Request kwargs:", kwargs)
        return Response({'message': 'OK'}, status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        print("Request Body:", request.query_params)
        print("All Func of request :", dir(request))
        print("Request args:", args)
        print("Request kwargs:", kwargs)
        # For All
        post = BlogPost.objects.all()
        categoryname = post.annotate(categoryname=F('category__name'))
        print("categoryname", categoryname)
        # For specific fields like only for 'title','post_body'
        post2 = BlogPost.objects.values_list('title', 'post_body')
        print('Query::', post2.values().query)
        print('Post Values::', post2)
        print("DIR QUERY", dir(post2))
        # print("post",list(post))
        # serializer = BlogPostSirializer(post, many=True)
        # print("serializer", serializer)
        return Response({"data": ""}, status=status.HTTP_200_OK)
        #return HttpResponse(BlogPost.objects.only('title'), content_type="application/json")

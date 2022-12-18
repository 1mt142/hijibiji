from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import BlogPost, BlogCategory

from django.db.models import F


# Create your views here.


class Blog(APIView):
    def get(self, request, pk=None):
        if pk is None:
            # query = BlogPost.objects.all().values('categories__name')
            query = BlogPost.objects.all().annotate(category=F('categories__name'), tag=F('tags__name')).values(
                'category', 'title', 'tag')

            return Response({'message': query})

    def post(self, request):
        print(request.data)
        if request.data:
            # many to many
            bp = BlogPost.objects.create(title=request.data['title'])
            bp.categories.add(request.data['categories'])
            print("-->", bp.categories.add(request.data['categories']))
            bp.tags.add(request.data['tags'])
            print(" bp Data :-", bp.categories)
            resp = {
                "title": bp.title,
                "cater": bp.categories.name
            }

            return Response(resp)

from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *

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


class PersonDetails(APIView):

    def get(self, request, *args, **kwargs):
        # *** getting all person data
        '''
        allPerson = Person.objects.all()
        print("allPerson:", allPerson)
        onePerson = Person.objects.get(id=3)
        print("onePerson:", onePerson)
        print("onePerson Mobile:", onePerson.mobile)
        print("Person Interest", onePerson.interests.all())
        for data in onePerson.interests.all():
            print("Interest:", data)
        # print("Person Address:", onePerson.personaddress)
        print("Person City:", onePerson.personaddress.city)
        print("Person Street:", onePerson.personaddress.street_address)
        '''
        print("Person data by City")
        city = City.objects.get(id=3)
        print("City :", city)
        all_person_address = city.personaddress_set.all()  # reverse relation _set.all()
        # we need reverse relation coz city do not have direct relation with person
        print("all Address with city", all_person_address)
        for data in all_person_address:
            print("Person Name:", data.person.name)

        interest = Interests.objects.get(id=2)
        print("interest:", interest)
        interest_person = interest.person_set.all()
        per = []
        for data in interest_person:
            per.append(data.name)
            print("interest_person:", data.name)

        return Response({"Data": per})

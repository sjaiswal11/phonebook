from django.shortcuts import render
from . serializers import ContactsModelSerializer
from . models import ContactsModel
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class ContactList(APIView):
    def get(self, request, format=None):
        snippets = ContactsModel.objects.all()
        serializer = ContactsModelSerializer(snippets, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ContactsModelSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ContactDetails(APIView):
    def get_object(self, name):
        try:
            return ContactsModel.objects.get(name = name)
        except ContactsModel.DoesNotExist:
            raise Http404

    def get(self, request, name, format=None):
        contact = self.get_object(name)
        serializer = ContactsModelSerializer(contact)
        return Response(serializer.data)

    def put(self, request, name, format=None):
        contact = self.get_object(name)
        serializer = ContactsModelSerializer(contact, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, name, format=None):
        contact = self.get_object(name)
        contact.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

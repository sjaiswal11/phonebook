from rest_framework import serializers
from . models import ContactsModel

class ContactsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactsModel
        fields = ['name', 'phone', 'user']
    
# DRF
from rest_framework import serializers
# Models
from ..models import Books


class BooksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Books
        fields = '__all__'
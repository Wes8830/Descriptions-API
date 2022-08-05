from rest_framework import serializers
from base.models import Columns, Categories, Sources

class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Columns
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['category', 'description', 'parentDir']

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sources
        fields = ['source', 'description', 'is_real_time']

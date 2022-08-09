from rest_framework import serializers
from django.contrib.auth.models import User
from base.models import Columns, Categories, Sources

class UserSerializer(serializers.ModelSerializer):
    columns = serializers.HyperlinkedRelatedField(many=True, view_name='columns-detail', read_only=True)

    class Meta:
        model = User
        fields = ['url', 'id', 'username', 'columns']

class ColumnSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    id = serializers.HyperlinkedIdentityField(view_name='column-highlight', format='html')

    class Meta:
        model = Columns
        fields = ['url', 'id', 'column', 'definition', 'description', 'parentDir', 'owner', 'created', 'updated']


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Categories
        fields = ['category', 'description', 'parentDir']

class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sources
        fields = ['source', 'description', 'is_real_time']

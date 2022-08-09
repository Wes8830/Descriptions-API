from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import reverse
# from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import renderers
from .permissions import IsOwnerOrReadOnly
from base.models import Columns
from django.http import Http404
from django.contrib.auth.models import User
from .serializers import UserSerializer, ColumnSerializer


@api_view(['GET'])
def home(request, format=None):
    return Response({
        'users': reverse('user-list', request=request, format=format),
        'columns': reverse('column-list', request=request, format=format)
    })


class UserList(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# Get All Columns, POST new column
class ColumnList(generics.ListCreateAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = Columns.objects.all()
    serializer_class = ColumnSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# GET single column, Update single column, Delete single column with the generics RetrievUpdateDestoryAPIView method
class ColumnItem(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Columns.objects.all()
    serializer_class = ColumnSerializer

class ColumnHighlight(generics.GenericAPIView):
    queryset = Columns.objects.all()
    renderer_classes = [renderers.StaticHTMLRenderer]

    def get(self, request, *args, **kwargs):
        column = self.get_object()
        return Response(column.id)





    

# class ColumnList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Columns.objects.all()
#     serializer_class = ColumnSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)


# class ColumnItem(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Columns.objects.all()
#     serializer_class = ColumnSerializer

#     def get(self, request, *args, **kwargs):
#         return self.get(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

# class ColumnList(APIView):
#     def get(self, request, format=None):
#         columns = Columns.objects.all()
#         serializer = ColumnSerializer(columns, many=True)
#         return Response(serializer.data)

#     def post(self, request, format=None):
#         serializer = ColumnSerializer(data=request.data)
        
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)

#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# class ColumnItem(APIView):
#     def get_object(self, pk):
#         try:
#             return Columns.objects.get(pk=pk)
#         except Columns.DoesNotExist:
#             raise Http404

#     def get(self, request, pk, format=None):
#         column = self.get_object(pk)
#         serializer = ColumnSerializer(column)
#         return Response(serializer.data)

#     def put(self, request, pk, format=None):
#         column = self.get_object(pk)
#         serializer = ColumnSerializer(column, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(status=status.HTTP_400_BAD_REQUEST)


#     def delete(self, request, pk, format=None):
#         column = self.get_object(pk)
#         column.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)



# Create from JSON File
# Create from csv File

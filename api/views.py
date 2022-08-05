from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from base.models import Columns
from .serializers import ColumnSerializer

# Get All Columns, POST new column
@api_view(['GET', 'POST'])
def columns(request, format=None):
    if request.method == 'GET':
        columns = Columns.objects.all()
        serializer = ColumnSerializer(columns, many=True)
        return Response(serializer.data)

    if request.method == 'POST':
        # serializer = ColumnSerializer(data=request.data)

        garbageCollector = []

        for item in request.data:
            serializer = ColumnSerializer(data=item)

            if serializer.is_valid():
                serializer.save()
            else: 
                garbageCollector.append(item)

        if garbageCollector:
            notSaved = garbageCollector

        return Response(f'The following objects were not saved:  {notSaved}', status=status.HTTP_201_CREATED)

        
    
    return Response("Oops, something is wrong with your request", status=status.HTTP_400_BAD_REQUEST)


# Read, Update and Delete operations for a single Column object
@api_view(['GET','PUT','DELETE'])
def columnItem(request, id, format=None):
    try: 
        column = Columns.objects.get(id=id)
    except:
        return Response("Column does not exist", status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = ColumnSerializer(column)

        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = ColumnSerializer(column, data=request.data)
        
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        column.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    

    return Response("Oops, something is wrong with your request", status=status.HTTP_400_BAD_REQUEST)



# Bulk Add Colums -> see about consolidating into get columns because it's not PK specific
@api_view(['POST'])
def bulkAdd(request):
    
    for item in request.data:
        serializer = ColumnSerializer(data=item)

        try:
            serializer.save()
        except:
            print(f'Did not write to database:\n"\n {item} \n"')

    return Response(request.data)


# Create from JSON File
# Create from csv File

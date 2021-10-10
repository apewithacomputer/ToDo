from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from .serializers import TodoSerializer
from .models import Todo
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


@api_view(['GET'])
def getRoutes(request):
    routes = [
        {
            'Endpoint': '/tasks/',
            'method': 'GET',
            'body': None,
            'description': 'Returns an array of tasks'
        },
        {
            'Endpoint': '/tasks/id/',
            'method': 'GET',
            'body': None,
            'description': 'Returns single tasks object'
        },
        {
            'Endpoint': '/tasks/creat/',
            'method': 'POST',
            'body': {'body': ""},
            'description': 'Creates new task with data sent in post request'
        },
        {
            'Endpoint': '/tasks/id/update/',
            'method': 'PUT',
            'body': {'body': ""},
            'description': 'Creates an existing task with data sent in post request'
        },
        {
            'Endpoint': '/tasks/id/delete/',
            'method': 'DELETE',
            'body': None,
            'description': 'Deletes an existing task'
        },
    ]
    return Response(routes)


@api_view(['GET'])
def getTasks(request):
    task = Todo.objects.all()
    serializer = TodoSerializer(task, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def getTask(request, pk):
    task = Todo.objects.get(id=pk)
    serializer = TodoSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['POST'])
def createTask(request):
    data = request.data
    task = Todo.objects.create(
        tasks=data['tasks']
    )
    serializer = TodoSerializer(task, many=False)
    return Response(serializer.data)


@api_view(['PUT'])
def updateTask(request, pk):
    data = request.data
    task = Todo.objects.get(id=pk)
    serializer = TodoSerializer(task, request.data)
    if serializer.is_valid:
        serializer.save()
    return Response(serializer.data)


@api_view(['DELETE'])
def deleteTask(request, pk):
    task = Todo.objects.get(id=pk)
    task.delete
    return Response('Task was deleted')

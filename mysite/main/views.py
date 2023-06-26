from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Crosses, Factory
from .serializers import CrossSerializer, CrossDetailSerializer, AnonymousRatingSerializer, FactorySerializer, \
    FactoryCreateUpdateSerializer


# Create your views here.

@api_view(['GET'])
def hello_world_view(request):
    return Response(data={'message: Hello world'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_crosses(request):
    if request.method == "GET":
        queryset = Crosses.objects.all()
        data = CrossSerializer(queryset, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        title = request.data.get('title')
        description = request.data.get('description')
        price = request.data.get('price')
        factory = request.data.get('factory')
        cross = Crosses.objects.create(title=title, description=description, price=price, factory_id=factory)
        return Response(data=CrossSerializer(cross, many=False).data)


@api_view(['GET', 'PUT'])
def retrieve_crosses(request, **kwargs):
    cross = Crosses.objects.get(id=kwargs.get('id'))
    if request.method == "GET":
        data = CrossDetailSerializer(cross, many=False).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "PUT":
        cross.title = request.data.get("title")
        cross.description = request.data.get('description')
        cross.price = request.data.get('price')
        cross.save()
        return Response(data=CrossSerializer(cross, many=False).data)


@api_view(['POST'])
def sent_anonymous_rating(request):
    serializer = AnonymousRatingSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        return Response(data={"message: Ok"}, status=status.HTTP_200_OK)
    return Response(data={"message: Error"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', "POST"])
def factory_view(request):
    if request.method == "GET":
        queryset = Factory.objects.all()
        data = FactorySerializer(queryset, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = FactoryCreateUpdateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
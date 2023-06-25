from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Crosses, Factory
from .serializers import CrossSerializer, CrossDetailSerializer, AnonymousRatingSerializer, FactorySerializer


# Create your views here.

@api_view(['GET'])
def hello_world_view(request):
    return Response(data={'message: Hello world'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_crosses(request):
    queryset = Crosses.objects.all()
    data = CrossSerializer(queryset, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['GET'])
def retrieve_crosses(request, **kwargs):
    queryset = Crosses.objects.get(id=kwargs.get('id'))
    data = CrossDetailSerializer(queryset, many=False).data
    return Response(data=data, status=status.HTTP_200_OK)


@api_view(['POST'])
def sent_anonymous_rating(request):
    serializer = AnonymousRatingSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        print(serializer.data)
        return Response(data={"message: Ok"}, status=status.HTTP_200_OK)
    return Response(data={"message: Error"}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def factory_view(request):
    queryset = Factory.objects.all()
    data = FactorySerializer(queryset, many=True).data
    return Response(data=data, status=status.HTTP_200_OK)
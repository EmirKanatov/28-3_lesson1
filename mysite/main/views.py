import django_filters
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status, mixins
from rest_framework.decorators import api_view
from rest_framework.generics import GenericAPIView, ListAPIView, ListCreateAPIView, RetrieveUpdateAPIView
from rest_framework.mixins import ListModelMixin, CreateModelMixin
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Crosses, Factory
from .serializers import CrossSerializer, CrossDetailSerializer, AnonymousRatingSerializer, FactorySerializer, \
    FactoryCreateUpdateSerializer, CrossModelSerializer
from rest_framework.viewsets import ModelViewSet, ReadOnlyModelViewSet, GenericViewSet


# Create your views here.

@api_view(['GET'])
def hello_world_view(request):
    return Response(data={'message: Hello world'}, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_crosses(request):
    if request.method == "GET":
        queryset = Crosses.objects.all()
        data = CrossModelSerializer(queryset, many=True).data
        return Response(data=data, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = CrossSerializer(data=request.data)

        serializer.is_valid(raise_exception=True)

        title = serializer.data.get('title')

        description = serializer.data.get('description')
        price = serializer.data.get('price')
        factory_id = serializer.data.get('factory_id')
        cross = Crosses.objects.create(title=title, description=description, price=price, factory_id=factory_id)

        return Response(data=CrossSerializer(cross, many=False).data)


class CrossApiView(ListCreateAPIView):
    queryset = Crosses.objects.all()
    serializer_class = CrossSerializer

    def get_serializer_class(self):
        return CrossModelSerializer if self.request.method == "GET" else CrossSerializer


class CrossesFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(field_name='title', lookup_expr='icontains')
    min_price = django_filters.NumberFilter(field_name="price", lookup_expr='price__gt')
    max_price = django_filters.NumberFilter(field_name="price", lookup_expr='price__lt')

    class Meta:
        model = Crosses
        fields = ['title']


class CrossModelViewSet(ModelViewSet):
    queryset = Crosses.objects.all()
    lookup_field = 'id'
    filterset_class = CrossesFilter
    filterset_fields = ['title']
    ordering_fields = ('price',)

    def get_serializer_class(self):
        return CrossModelSerializer if self.action in ("list", 'retrieve') else CrossSerializer

    def create(self, request, *args, **kwargs):
        serializer = CrossSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.data.get('title')
        description = serializer.data.get('description')
        price = serializer.data.get('price')
        factory_id = serializer.data.get('factory_id')
        cross = Crosses.objects.create(title=title, description=description, price=price, factory_id=factory_id)

        return Response(data=CrossSerializer(cross, many=False).data)

    def update(self, request, *args, **kwargs):
        serializer = CrossSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        title = serializer.data.get('title')
        description = serializer.data.get('description')
        price = serializer.data.get('price')
        factory_id = serializer.data.get('factory_id')
        cross = Crosses.objects.create(title=title, description=description, price=price, factory_id=factory_id)

        return Response(data=CrossSerializer(cross, many=False).data)


# class UpdateDestroyCrossesModelViewSet(GenericViewSet, mixins.UpdateModelMixin,mixins.DestroyModelMixin):


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


class RetrieveUpdateCrossesAPIView(RetrieveUpdateAPIView):
    queryset = Crosses.objects.all()
    serializer_class = CrossDetailSerializer



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
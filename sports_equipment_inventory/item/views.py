import logging
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import HTTP_201_CREATED, HTTP_200_OK, HTTP_400_BAD_REQUEST, HTTP_404_NOT_FOUND, HTTP_500_INTERNAL_SERVER_ERROR
from .models import Item
from .serializers import ItemSerializer


logger = logging.getLogger(__name__)


class ItemAPIView(APIView):
    
    def get(self, request):
        
        filter_query = Q()
        items = []
        
        available = self.request.GET.get('available', "")
        available = available.lower()
        if available == "false":
            filter_query = Q(quantity=0)
        elif available == "true":
            filter_query = Q(quantity__gt=0)

        items = Item.objects.filter(filter_query)
        serializer = ItemSerializer(items, many=True)
        return Response({"message": "Success", "data": serializer.data}, status=HTTP_200_OK)

    def post(self, request):

        if "name" not in request.data:
            return Response({"message": "Error",  "data": "Name required"}, status=HTTP_400_BAD_REQUEST)

        serializer = ItemSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Success", "data": serializer.data}, status=HTTP_201_CREATED)
        return Response({"message": "Error",  "data": serializer.errors}, status=HTTP_400_BAD_REQUEST)

    def put(self, request, pk):
        try:
            instance = Item.objects.get(id=pk)
            serializer = ItemSerializer(instance, data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"message": "Success", "data": serializer.data}, status=HTTP_201_CREATED)
            return Response({"message": "Error", "data": serializer.errors}, status=HTTP_400_BAD_REQUEST)
        except Item.DoesNotExist:
            return Response({"message": "Item does not exist", "data": []}, status=HTTP_404_NOT_FOUND)
        except Exception as e:
            logger.error(e)
            return Response({"message": "Something went wrong", "data": []}, status=HTTP_500_INTERNAL_SERVER_ERROR)

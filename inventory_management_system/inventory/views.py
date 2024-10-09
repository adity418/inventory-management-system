import logging
from django.core.cache import cache
from rest_framework import viewsets,  status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import InventoryItem
from .serializer import InventoryItemSerializer

logger = logging.getLogger(__name__)

class InventoryItemViewSet(viewsets.ModelViewSet):
    queryset = InventoryItem.objects.all()
    serializer_class = InventoryItemSerializer
    permission_classes = [IsAuthenticated]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            if InventoryItem.object.filter(name=serializer.validated_data['name']).exists():
                logger.error(f"Item already exists: {serializer.validated_data['name']}")
                return Response({'error':'Item already exists'}, status=status.HTTP_400_BAD_REQUEST)
            self.perform_create(serializer)
            logger.info(f"Item created : {serializer.data['name']}")
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        logger.error(f"Invalid data for item creation : {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        cache_key =f'item_{instance.id}'
        cached_data -cache.get(cache_key)

        if cached_data:
            logger.info(f"Retreived item from cache: {instance.name}")
            return Response(cached.data)
        
        serializer = self.get_serializer(instance)
        cache.set(cache_key, serializer.data, timeout=300) # cache for 5 min
        logger.info(f"Retrieved item from database and cached: {instance.name}")
        return Response(serializer.data)
    
    def update(self, request, *args, **kwargs):
        partial = kwargs.pop('partial', False)
        instance = self.get_object()
        serializer =  self.get_serializer(instance, data=request.data, partial=partial)
        if serializer.is_valid():
            self.perform_update(serializer)
            cache_key = f"item_{instance.id}"
            cache.delete(cache_key)
            logger.info(f"Item updated: {instance.name}")
            return Response(serializer.data)
        logger.error(f"Invalid data for item update: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        cache_key = f'item_{instance.id}'
        cache.delete(cache_key)
        self.perforn_destroy(instance)
        logger.info(f"Item deleted : {instance.name}")
        return response(status=status.HTTP_204_NO_CONTENT)
from .models import Guitar
from rest_framework import viewsets, permissions
from .serializers import GuitarSerializer

class GuitarViewSet(viewsets.ModelViewSet):
    #Everything in the guitar object (which is everything -everything)
    queryset=Guitar.objects.all()
    # sepcificies the which serializer to use. In this case, we will be use the file: TodoSerializer to do the serialization and deserialization
    serializer_class=GuitarSerializer
    # unrestricted access to the api
    permission_classes=[permissions.AllowAny]
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import user_info
from .serializers import user_ser

class user_info_view(APIView):
    def post(self, request, format=None):
        serializer = user_ser(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class list_users(APIView):
    def get(self, request, format=None):
        instances = user_info.objects.all()
        serializer = user_ser(instances, many=True)
        return Response(serializer.data)
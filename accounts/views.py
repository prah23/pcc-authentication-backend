from django.shortcuts import render
from .serializers import UserInfoSerializer, UserModifySerializer
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from django.contrib.auth import get_user_model

# Create your views here.

User = get_user_model()


def home(response):
    return render(response, "home.html", {})


class UserDetailsView(APIView):

    def get(self, request):
        try:
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            serializer = UserInfoSerializer(
                user, context={'request':request}
            )
            return Response(serializer.data, status=200)
        except User.DoesNotExist:
            return Response({
                'status': 'error',
            }, status=400)
    
    def patch(self, request):
        user_id = request.user.id
        try:
            user = User.objects.get(id=user_id)
            serializer = UserModifySerializer(
                user, data=request.data, partial=True, context={'request':request}
            )
            if serializer.is_valid():
                serializer.save()
            return Response(serializer.data, status=200)
        except User.DoesNotExist:
            return Response({
                'status': 'error',
            }, status=400)
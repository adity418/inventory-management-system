from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User
from .serializer import UserSerializer
import logging

logger = logging.getLogger(__name__)

# Create your views here.

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            logger.info(f"User registered: ,{user.username}")
            return Response({
                'refresh': str(refresh),
                'access': str(refresh.access_token),
            }, status=status.HTTP_201_CREATED)
        logger.erroe(f"Invalid registration data: {serializer.errors}")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LoginView(APIView):

    def post(self,request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = User.objects.filter(username=username).first()

        if user is None or not user.check_password(password):
            logger.erroe(f"Invalid login attempt for user: {username}")
            return Response({'errror':'Invalid crediantials'}, status=status.HTTP_400_BAD_REQUEST)
        
        refresh = RefreshToken.for_user(user)
        logger.info(f"User logged in: {username}")
        return Response({
            'refresh': str(refresh),
            'access': str(refresh.access_token),
        })
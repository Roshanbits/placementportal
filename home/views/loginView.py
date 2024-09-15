# home/views.py
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from home.models import User
from home.serializers import CustomUserSerializer
from home.serializers import LoginSerializer

#Login The User
class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            return Response({'message': 'Login successful.'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#Create User
class CustomUserView(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = CustomUserSerializer(users, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CustomUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            return Response("User Created Successfully", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class HomeView(APIView):
    def get(self, request):
        
        pi_data = [1,2,3,4,5,6,7,8]
        
        response_data = {
            "pi_data" : pi_data
        }
        return Response(response_data, status=status.HTTP_200_OK)
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import *
from .serializers import *

from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated

from django.contrib.auth import authenticate

#TOken Generate Manually
def get_tokens_for_user(user):
    

    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }
    
    

class UserRegistrationView(APIView):
    def post(self,request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save() 
            
            token = get_tokens_for_user(user)
            
            return Response({'message':'Registration Successful!',
                             'token':token,
                             'user': serializer.data,}, 
                            status=status.HTTP_201_CREATED)
        return Response({'message':'Registration Not Completed!',
                         'user':serializer.errors,},status=status.HTTP_400_BAD_REQUEST)
        


class LoginView(APIView):
    def post(self,request):
        serializer = LoginSerializer(data = request.data)
        if serializer.is_valid():
            email = serializer.data.get('email')
            password = serializer.data.get('password')
            user = authenticate(request, email = email, password = password)
            
            if user is not None:
                token = get_tokens_for_user(user)
                
                return Response({'token':token,'message': 'Login Successful'}, status=status.HTTP_200_OK)
            else:
                return Response({'message': 'Invalid email or password'}, status=status.HTTP_401_UNAUTHORIZED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self,request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data,status=status.HTTP_200_OK) 
    
class ChangePasswordView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self,request):
        serializer = ChangePasswordSerializer(data = request.data)
        if serializer.is_valid():
            user = request.user #logged in user
            password = serializer.validated_data.get('password') #get that validate password
            user.set_password(password) #hash password
            user.save() #then save the password
            return Response({'message': 'Password Changed!'}, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ResetPasswordView(APIView):
    def post(self,request):
        serializer = PasswordResetSerializer(data = request.data)
        if serializer.is_valid():
            return Response({'message':'Password reset link send!'},status=status.HTTP_200_OK)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)            
    
class ConfirmPasswordView(APIView):
    def post(self, request, uid, token):
        data = {
            "uid": uid,
            "token": token,
            "password": request.data.get("password"),
            "password2": request.data.get("password2"),
        }
        serializer = ConfirmPasswordSerializer(data=data)
        if serializer.is_valid():
            user = serializer.validated_data['user']
            password = serializer.validated_data['password']
            user.set_password(password)
            user.save()
            return Response({'message': 'Password changed successfully!'}, status=200)
        return Response(serializer.errors, status=400)

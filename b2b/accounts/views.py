
# views.py
from rest_framework import generics, status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.decorators import api_view, permission_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from django.contrib.auth import authenticate
from django.shortcuts import get_object_or_404
from django.db import transaction
from .models import Profile
from .serializers import (
    RegisterSerializer, 
    LoginSerializer, 
    UserSerializer
)

class RegisterProfileView(generics.CreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        
        try:
            with transaction.atomic():
                user = serializer.save(is_verified=True)
                user.save()
                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error during registration: {str(e)}")  # Add this line for server-side debugging
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def register(request):
    serializer = RegisterSerializer(data=request.data)
    
    if serializer.is_valid():
        try:
            with transaction.atomic():
                user = serializer.save(is_verified=True)
                user.save()

                return Response(UserSerializer(user).data, status=status.HTTP_201_CREATED)
        except Exception as e:
            print(f"Error during registration: {str(e)}")  # Add this line for server-side debugging
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import LoginSerializer

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    """
    API view to authenticate a user and set an access token cookie on successful login.
    """
    serializer = LoginSerializer(data=request.data)
    if serializer.is_valid():
        user = serializer.validated_data  # The validated data contains the user instance

        # Generate JWT tokens
        refresh = RefreshToken.for_user(user)
        response_data = {
            'message': 'Login successful',
            'user': {
                'id': user.id,
                'username': user.username,
                'email': user.email
            }
        }
        response = Response(response_data, status=status.HTTP_200_OK)
        
        # Set access token cookie
        access_token = str(refresh.access_token)
        response.set_cookie(
            key='access_token', 
            value=access_token,
            httponly=True,
            secure=False,  
            samesite='Lax',
            max_age=3600
        )
        
        # Print the access token cookie to the console
        print(f"Access Token Cookie: {access_token}")
        
        return response

    # Return errors if serializer is not valid
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request):
        try:
            response = Response({'message': 'Logout successful'})
            response.delete_cookie('access_token')
            return response
        except Exception as e:
            return Response(
                {'detail': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

class FollowView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        try:
            profile_to_follow = get_object_or_404(Profile, pk=pk)
            if profile_to_follow == request.user.profile:
                return Response(
                    {"detail": "You cannot follow yourself"},
                    status=status.HTTP_400_BAD_REQUEST
                )
            
            request.user.profile.follow(profile_to_follow)
            serializer = UserSerializer(
                profile_to_follow,
                context={'request': request}
            )
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'detail': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

class UnfollowView(APIView):
    permission_classes = [IsAuthenticated]
    
    def post(self, request, pk):
        try:
            profile_to_unfollow = get_object_or_404(Profile, pk=pk)
            request.user.profile.unfollow(profile_to_unfollow)
            serializer = UserSerializer(
                profile_to_unfollow,
                context={'request': request}
            )
            return Response(serializer.data)
        except Exception as e:
            return Response(
                {'detail': str(e)}, 
                status=status.HTTP_400_BAD_REQUEST
            )

class ProfileDetailView(generics.RetrieveAPIView):
    queryset = Profile.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework_simplejwt.exceptions import InvalidToken, TokenError

@api_view(['GET'])
def auth_check(request):
    jwt_auth = JWTAuthentication()
    try:
        validated_token = jwt_auth.get_validated_token(request.COOKIES.get('access_token'))
        user = jwt_auth.get_user(validated_token)
        return Response({'isAuthenticated': True, 'user': user.phone_number})
    except (InvalidToken, TokenError):
        return Response({'isAuthenticated': False}, status=status.HTTP_401_UNAUTHORIZED)









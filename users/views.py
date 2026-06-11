from django.shortcuts import render
import uuid 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from .serializers import UserSerializer
from .models import User

class UserListCreateView(APIView) :
    
    @extend_schema(
        summary="Get all users",
        description="Returns a list of all users stored in memory."
    )
    def get(self, request) :
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @extend_schema(
        summary="Create a new user",
        description="Creates a new user and stores it in memory."
    )
    def post(self, request) :
        serializer = UserSerializer(data = request.data)
        
        if serializer.is_valid() : 
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

class UserDetailView(APIView):

    def get_object(self, user_id):
        try:
            return User.objects.get(
                id=user_id
            )
        except User.DoesNotExist:
            return None
        
        
    @extend_schema(
        summary="Get a specific user",
        description="Returns the details of a user identified by their ID."
    )
    def get(self, request, user_id):

        user = self.get_object(user_id)
        if not user:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    
    @extend_schema(
        summary="Update a specific user",
        description="Updates the details of a user identified by their ID."
    )
    def put(self, request, user_id):
        user = self.get_object(user_id)
        if not user:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_OK)

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


    @extend_schema(
        summary="Delete a specific user",
        description="Deletes a user identified by their ID."
    )
    def delete(self, request, user_id):
        user = self.get_object(user_id)
        if not user:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        user.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
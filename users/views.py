from django.shortcuts import render
import uuid 
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_spectacular.utils import extend_schema

from .serializers import UserSerializer
from .storage import USERS


class UserListCreateView(APIView) :
    @extend_schema(
        summary="Get all users",
        description="Returns a list of all users stored in memory."
    )
    def get(self, request) :
        return Response(list(USERS.values()), status=status.HTTP_200_OK)
    
    @extend_schema(
        summary="Create a new user",
        description="Creates a new user and stores it in memory."
    )
    def post(self, request) :
        serializer = UserSerializer(data = request.data)
        
        if serializer.is_valid() : 
            user_id = uuid.uuid4()
            
            user_data = {
                "id": user_id,
                "name": serializer.validated_data["name"],
                "email": serializer.validated_data["email"],
                "age": serializer.validated_data["age"]
            }
        
            USERS[str(user_id)] = user_data
        
            return Response(user_data, status=status.HTTP_201_CREATED)
    
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 


class UserDetailView(APIView):

    @extend_schema(
        summary="Get a specific user",
        description="Returns the details of a user identified by their ID."
    )
    def get(self, request, user_id):

        user = USERS.get(str(user_id))

        if not user:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        return Response(
            user,
            status=status.HTTP_200_OK
        )

    @extend_schema(
        summary="Update a specific user",
        description="Updates the details of a user identified by their ID."
    )
    def put(self, request, user_id):

        user = USERS.get(str(user_id))

        if not user:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        serializer = UserSerializer(data=request.data)

        if serializer.is_valid():

            updated_user = {
                "id": user["id"],
                "name": serializer.validated_data["name"],
                "email": serializer.validated_data["email"],
                "age": serializer.validated_data["age"]
            }

            USERS[str(user_id)] = updated_user

            return Response(
                updated_user,
                status=status.HTTP_200_OK
            )

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )

    @extend_schema(
        summary="Delete a specific user",
        description="Deletes a user identified by their ID."
    )
    def delete(self, request, user_id):

        user = USERS.get(str(user_id))

        if not user:
            return Response(
                {"error": "User not found"},
                status=status.HTTP_404_NOT_FOUND
            )

        del USERS[str(user_id)]

        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
        
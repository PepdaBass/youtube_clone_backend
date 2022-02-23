from django.http import Http404
from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.decorators import api_view, permission_classes
from .models import Comment, Reply
from .serializers import CommentSerializer, ReplySerializer
from django.contrib.auth.models import User

# Create your views here.

#----------------Comment Class-------------

@api_view(['GET'])
@permission_classes([AllowAny])
def get_all_comments(request):
  comments = Comment.objects.all()
  serializer = CommentSerializer(comments, many=True)
  return Response(serializer.data)


@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def create_comment(request):
  if request.method == 'POST':
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'GET':
    comments = Comment.objects.filter(user_id=request.user.id)
    serializer = CommentSerializer(comments, many=True)
    return Response(serializer.data)
  




#----------------Reply Class-------------

#class ReplyList(APIView):

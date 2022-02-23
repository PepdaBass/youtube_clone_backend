from math import perm
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

#----------------Comment Function Views-------------

@api_view(['GET'])
@permission_classes([AllowAny])
def get_video_comments(request, video_id):
  comments = Comment.objects.filter(video_id=video_id)
  serializer = CommentSerializer(comments, many=True)
  return Response(serializer.data)



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_comment(request):
  if request.method == 'POST':
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def edit_comment(request, pk):
  try:
    comment = Comment.objects.get(pk=pk)
  except Comment.DoesNotExist:
      raise Http404
  serializer = CommentSerializer(comment, data=request.data)
  if serializer.is_valid():
    serializer.save()
    return Response(serializer.data, status=status.HTTP_200_OK)
  return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


#----------------Reply Function Views-------------


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def get_comment_replies(request, comment_id):
  replies = Reply.objects.filter(comment_id=comment_id)
  serializer = ReplySerializer(replies, many=True)
  return Response(serializer.data)
        

@api_view(['POST', 'GET'])
@permission_classes([IsAuthenticated])
def create_reply(request):
  if request.method == 'POST':
    serializer = ReplySerializer(data=request.data)
    if serializer.is_valid():
      serializer.save(user=request.user)
      return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  elif request.method == 'GET':
    reply = Reply.objects.filter(user_id=request.user.id)
    serializer = ReplySerializer(reply, many=True)
    return Response(serializer.data)
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

class CommentList(APIView):

  permission_classes = [AllowAny]
 
  # def get_object(self, pk):
  #   try:
  #       return Comment.objects.get(pk=pk)
  #   except Comment.DoesNotExist:
  #     raise Http404

  def get(self, request):
      comments = Comment.objects.all()
      serializer = CommentSerializer(comments, many=True)
      return Response(serializer.data)

  # def put(self, request, pk):
  #     comment = self.object(pk)
  #     serializer = CommentSerializer(comment, data=request.data)
  #     if serializer.is_valid():
  #       serializer.save()
  #       return Response(serializer.data)
  #     return Response(Http404)




#----------------Reply Class-------------

class ReplyList(APIView):

  permission_classes = [AllowAny]
 
  # def get_object(self, pk):
  #   try:
  #       return Reply.objects.get(pk=pk)
  #   except Reply.DoesNotExist:
  #     raise Http404

  def get(self, request):
      replies = Reply.objects.all()
      serializer = ReplySerializer(replies, many=True)
      return Response(serializer.data)

  # def put(self, request, pk):
  #     reply = self.object(pk)
  #     serializer = ReplySerializer(reply, data=request.data)
  #     if serializer.is_valid():
  #       serializer.save()
  #       return Response(serializer.data)
  #     return Response(Http404)
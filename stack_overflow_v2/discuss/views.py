import imp
from urllib import response
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view,permission_classes
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly,IsAdminUser
from yaml import serialize
from .serializers import *
from django.contrib.auth import login
from rest_framework import status,serializers
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from rest_framework import status
import datetime
# from datetime import datetime
# Create your views here.

class Register(APIView):
    def get(self,request):
        query = Users.objects.all()
        serialize = UsersSerializer(query,many=True)
        return Response(serialize.data)
    def post(self,request):
        print(request.data)
        username = request.data["username"]
        pass1 = request.data["password"]
        pass2 = request.data["conf_password"]
        if pass1!= pass2:
            raise serializers.ValidationError("finish must occur after start")
        user =User.objects.create_user(password = pass1,username = username)
        user.save()
        login(request,user)

        format = "%Y-%m-%d"
        # dt_object = datetime.datetime.strptime(request.data["dob"], format)
        # print(type(request.data["dob"]))
        # date_time = request.data["dob"].strftime("%Y/%m/%d")
        data = {"user":user,"dob":request.data["dob"]}
        ret_data = {"status": "Account successfully created",
        "status_code":status.HTTP_201_CREATED

        }
        serializer = UsersSerializer(data= data)

        user_data = {
            "user_id": user.id,
            "account_state": "ACTIVE"
        }
        ret_data["json-data"]: user_data
        if serializer.is_valid():
            user1 = Users.objects.create(user= user, dob=request.data["dob"])
            user1.save()
            # ret_data["status"] = "Account successfully created"
            
            
            return Response("registered")
        return Response(ret_data)

@api_view(["GET"])
@permission_classes([IsAuthenticated])
def logout_view(request):
    user = request.user
    logout(request=request)
    return Response("successfully logged out {}".format(user.username))



class ListQuestions(APIView):
    def get(self,request):
        questions = Questions.objects.all()
        serial = QuestionSerializer(questions,many=True)
        return Response(serial.data)
    permission_classes = [IsAuthenticatedOrReadOnly]
    def post(self,request):
        serialize = QuestionSerializer(data=request.data)
       
        
        if serialize.is_valid():
            print(serialize.validated_data)
            serialize.save()
            quest = Questions.objects.get(question_title=serialize.validated_data['question_title'])
            ret_data = {
            "status": 'success',
            "status_code": status.HTTP_201_CREATED,
            "question_id": quest.id,
                }
            return Response(ret_data)


class BlockUser(APIView):
    permission_classes= [IsAdminUser]
    def post(self,request,pk):
        reason = "Using vulgar languages in question"
        ret_data = {}
        if request.data['reason']!= reason:
            ret_data["error"]  = "your reason is not appropriate"
        else:
            user = Users.objects.get(pk=pk)
            user.account_state = False
            user.save()
            ret_data["status"] = "success",
            ret_data["status_code"] = 200
        return Response(ret_data)
class UnBlockUser(APIView):
    permission_classes= [IsAdminUser]
    def post(self,request,pk):
        reason = "Have edited the questions"
        ret_data = {}
        if request.data['reason']!= reason:
            ret_data["error"]  = "your reason is not appropriate"
        else:
            user = Users.objects.get(pk=pk)
            user.account_state = True
            user.save()
            ret_data["status"] = "success",
            ret_data["status_code"] = 200
        return Response(ret_data)

class BlockQuestion(APIView):
    permission_classes= [IsAdminUser]
    def post(self,request,pk):
        reason = "Used vulgar languages in question"
        ret_data = {}
        if request.data['reason']!= reason:
            ret_data["error"]  = "your reason is not appropriate"
        else:
            user = Questions.objects.get(pk=pk)
            user.is_blocked = True
            user.save()
            ret_data["question_id"] = user.id
            ret_data["status"] = "success",
            ret_data["status_code"] = status.HTTP_200_OK
        return Response(ret_data)

class UnBlockQuestion(APIView):
    permission_classes= [IsAdminUser]
    def post(self,request,pk):
        reason = "Have edited the question"
        ret_data = {}
        if request.data['reason']!= reason:
            ret_data["error"]  = "your reason is not appropriate"
        else:
            user = Questions.objects.get(pk=pk)
            user.is_blocked = False
            user.save()
            ret_data["question_id"] = user.id
            ret_data["status"] = "success",
            ret_data["status_code"] = status.HTTP_200_OK
        return Response(ret_data)
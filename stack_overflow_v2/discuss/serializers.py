from rest_framework import serializers,fields
from .models import *
from django.contrib.auth.models import User


class UsersSerializer(serializers.ModelSerializer):
    dob = fields.DateField(input_formats=['%Y-%m-%d'])
    class Meta:
        
        
        model = Users
        fields = ["user","dob"]
    


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Questions
        fields = ["question_title","question_body"]
   
    
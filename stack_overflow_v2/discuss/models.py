from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class Users(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dob = models.DateField()
    account_state = models.BooleanField(default=True)
 
class Questions(models.Model):
    question_title  = models.TextField(max_length=50)
    question_body  = models.TextField(max_length=500)
    q_upvotes = models.IntegerField(default=0)
    q_downvotes = models.IntegerField(default=0)
    is_blocked = models.BooleanField(default=False)
    is_deleted = models.BooleanField(default=False)
    # answers = models.ForeignKey(Answers,on_delete=models.CASCADE)


    
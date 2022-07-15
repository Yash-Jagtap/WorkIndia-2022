from django.urls import path,include
from .views import *

urlpatterns = [
path("users/",Register.as_view(),name="registerUser"),
path("questions/",ListQuestions.as_view(),name="questions"),
path("users/<int:pk>/block/",BlockUser.as_view(),name="blockuser"),
path("users/<int:pk>/unblock/",UnBlockUser.as_view(),name="unblockuser"),
path("questions/<int:pk>/block/",BlockQuestion.as_view(),name="BlockQuestion"),
path("questions/<int:pk>/unblock/",UnBlockQuestion.as_view(),name="UnBlockQuestion"),
]
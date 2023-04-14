from django.urls import path
from . import views

urlpatterns = [
    path('', views.FollowerList.as_view()),
    path('<int:pk>/', views.FollowerDetail.as_view()),
    path('following_<str:followed_name>/', views.FollowingList.as_view()),
    path('followed_by_<str:owner>/', views.FollowedByList.as_view()),

]

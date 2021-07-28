from django.urls import path
from base.views import user_view as views


urlpatterns = [
    path('login/', views.MyTokenObtainPairView.as_view(),
         name='token_obtain_pair'),


    path('register/', views.registerUser, name="register"),
    path('', views.getUsers, name="user-profile"),
    path('delete/<str:pk>/', views.deleteUser, name='user-delete'),
    path('profile/', views.getUserProfile, name="user-profile"),
    path('profile/update/', views.updateUserProfile, name="user-profile-update"),
    path('<str:pk>/', views.getUserById, name="user"),
    path('update/<str:pk>/', views.updateUser, name="user-update"),

]

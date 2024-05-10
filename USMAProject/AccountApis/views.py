from django.shortcuts import render,redirect


# Create your views here.
from django.shortcuts import render,get_object_or_404
from Apis.serializers import *
from USMAApp.models import *
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib import messages


#REST FRAMEWORK
from rest_framework import status
from rest_framework.response import Response

#---------------------FUNCTION VIEW-------------------------
from rest_framework.decorators import api_view

#------------------------CLASS BASED VIEW-------------------
from rest_framework.views import APIView


#------------------------GENERIC VIEWs-------------------
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView


#------------------------ VIEW SETS-------------------
from rest_framework.viewsets import ModelViewSet


#------FILTERS, SEARCH AND ORDERING
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.filters import SearchFilter,OrderingFilter

#------PAGINATION-------------
from rest_framework.pagination import PageNumberPagination




#----------------CREATING A CART------------------------
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet

from Apis.serializers import *
from drf_yasg.utils import swagger_auto_schema

from rest_framework import generics,status
from rest_framework.decorators import api_view

# Create your views here.

# class UserView(APIView):

# 	def get(self,request, format=None):
# 		return Response("User Account View", status=200)

# 	def post(self,request, format=None):

# 		return Response("Creating User", status=200)



from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView



import jwt, datetime
from rest_framework.exceptions import AuthenticationFailed


from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# class RegistrationView(generics.CreateAPIView):
#     queryset = MyUser.objects.all()
#     serializer_class = DjangoReactUserSerializer
#     permission_classes = (permissions.AllowAny,)

# class ReactLoginView(generics.CreateAPIView):
#     queryset = User.objects.all()
#     serializer_class = DjangoReactUserSerializer
    
#     def create(self, request, *args, **kwargs):
#         user = self.get_object()
#         token, created = Token.objects.get_or_create(user=user)
#         return Response({'token': token.key})


from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authtoken.models import Token



# SIGNIN YA KAWAIDA SIO YA APIS
def signin(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.info(request, 'Credentials Invalid, Username or Password is incorrect')
            return redirect('home')

    else:
        return render(request, 'USMAApp/home.html')


def logout(request):
    auth.logout(request)
    return redirect('home')


# SIGNUP YA KAWAIDA SIO YA APIS
def signup(request):

    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']
        password2 = request.POST['password2']

        if password == password2:
            if MyUser.objects.filter(email=email).exists():
                messages.info(request, 'Email Already Taken')
                return redirect('home')
            elif MyUser.objects.filter(username=username).exists():
                messages.info(request, 'Username Already Taken')
                return redirect('home')
            else:
                user = MyUser.objects.create_user(username=username, email=email, password=password)
                user.save()



                #log user in and redirect to settings page
                user_login = auth.authenticate(email=email, password=password)
                auth.login(request, user_login)

                messages.success(request, f'You have registered successfully as {username} ')
                return redirect('home')

                
        else:
            messages.info(request, 'Password Not Matching')
            return redirect('home')

    # else:
    #     return render(request, 'USMAApp/home.html')

















#----------------HIZI NI KWA AJILI YA APIS ------------------------------
class RegistrationView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data.get('email')
            password = serializer.validated_data.get('password')
            username = serializer.validated_data.get('username')
            phone = serializer.validated_data.get('phone')
            # last_name = serializer.validated_data.get('last_name')
            
            if MyUser.objects.filter(email=email).exists():
                return Response({'error': 'email already exists'}, status=status.HTTP_400_BAD_REQUEST)
            
            user = MyUser.objects.create_user(email=email, password=password, username=username, phone=phone)
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Registration failed'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReactLoginView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')
        password = request.data.get('password')
        
        user = authenticate(email=email, password=password)
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key})
        else:
            return Response({'error': 'Invalid credentials'}, status=400)





class LogoutView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    
    def post(self, request, *args, **kwargs):
        user = request.user
        if user.is_authenticated:
            Token.objects.filter(user=user).delete()
            return Response({'message': 'Logged out successfully'}, status=status.HTTP_200_OK)
        else:
            return Response({'error': 'User not authenticated'}, status=status.HTTP_401_UNAUTHORIZED)





class UserDataView(APIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        user = request.user
        # Assuming you have a serializer for User data
        serializer = UserDataSerializer(user)
        return Response(serializer.data)


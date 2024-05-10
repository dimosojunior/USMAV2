from django.shortcuts import render
from django.shortcuts import render,redirect

from django.http import HttpResponse
# Create your views here.
from django.shortcuts import render,get_object_or_404
from Apis.serializers import *
from .models import *
from Apis.serializers import *
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
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def home(request):

	return render(request, 'USMAApp/home.html')


#-------------ALL UNIVERSITIES---------
# EG: http://127.0.0.1:8000/GetAllUniversities/?page=1&page_size=2
class GetAllUniversitiesView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            
            


            queryset = Universities.objects.all()
            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = UniversitiesSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)










#---------ALL COURSES ACCORDING TO EACH UNIVERSITY----------
# Eg:http://127.0.0.1:8000/GetAllUniversitiesCourses/?id=9&page=1&page_size=2
class GetAllUniversitiesCoursesView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            categoryId = int(request.query_params.get('universityId'))
            


            queryset = UniversityCourses.objects.filter(
                university__id__icontains = categoryId
                )

            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = UniversityCoursesSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)









#-------------------ALL PROJECTS FOR EACH UNIVERSITY----------------

class GetAllProjectsView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            
            universityId = int(request.query_params.get('universityId'))

            # hapa tusitumie id kufilter kwasababu kwenye model ya 
            # UniversityCourses unaweza kuta the same course zimetokea
            # zaidi ya mara moja ko huwezi kujua inayopatikana labda MUST
            # ina id gani ko tumia jina tu la kozi
            #Eg: http://127.0.0.1:8000/GetAllProjects/?universityId=2&CourseName=Computer Engineering&page=1&page_size=5
            #-------------------------------------
            #courseId = int(request.query_params.get('id'))
            course_name = request.query_params.get('CourseName')
            


            queryset = AllProjects.objects.filter(
                university__id__icontains = universityId,
                CourseName__CourseName__icontains = course_name
                )

            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = AllProjectsSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)

















            #-------------------------ARTICLES--------------------------


class GetAllArticlesView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            
            


            queryset = Articles.objects.all()
            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = ArticlesSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)










#---------ALL ARTICLES CATEGORY----------

class GetAllArticlesCategoryView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            articleId = int(request.query_params.get('id'))
            


            queryset = ArticlesCategory.objects.filter(
                ArticlesName__id__icontains = articleId
                )

            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = ArticlesCategorySerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




















            #-------------------------EXPERT--------------------------


class GetAllHobView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            
            


            queryset = Hob.objects.all()
            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = HobSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)










#---------ALL EXPERTS CATEGORY----------

class GetAllExpertCategoryView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            hobId = int(request.query_params.get('id'))
            


            queryset = Experts.objects.filter(
                CategoryName__id__icontains = hobId
                )

            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = ExpertsSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)











#------------------PEOPLE WORKS-------------------

class GetAllPeopleWorksCategoryView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            
            


            queryset = PeopleWorksCategory.objects.all()
            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = PeopleWorksCategorySerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)




class GetAllPeopleWorksView(APIView):
    def get(self, request):
        try:
            # Get the page number from the query parameters, default to 1
            page = int(request.query_params.get('page', 1))
            page_size = int(request.query_params.get('page_size', 5))  # Adjust page size as needed
            CategoryID = int(request.query_params.get('id'))
            


            queryset = PeopleWorks.objects.filter(
                Category__id__icontains = CategoryID
                )

            # # Use pagination to get the desired page
            paginator = PageNumberPagination()
            paginator.page_size = page_size
            page_items = paginator.paginate_queryset(queryset, request)

            serializer = PeopleWorksSerializer(page_items, many=True)

            response_data = {
                'queryset': serializer.data,
                'total_pages': paginator.page.paginator.num_pages,  # Send total pages info
                'current_page': page,  # Send current page info
            }

            return Response(response_data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e), "queryset":[]}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)












#--------------------CREATE DATA ------------------------

class CreateNewProject(APIView):
    def post(self, request, format=None):
        serializer = AllProjectsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            #Send message to all user when new data is added
            queryset = MyUser.objects.all()
            for x in queryset:
                # Send an email to the user
                email = x.email
                subject = "Students Projects Share"
                message = f"Hello {x.username}, a new project has been added to the Students Projects Share App.\n \n Please visit our application to see more. \n \n Click on the link below to be the first. \n https://play.google.com/store/apps/details?id=ttpc.StudentsProjectsShare"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class CreateNewArticle(APIView):
    def post(self, request, format=None):
        serializer = ArticlesCategorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            #Send message to all user when new data is added
            queryset = MyUser.objects.all()
            for x in queryset:
                # Send an email to the user
                email = x.email
                subject = "Students Projects Share"
                message = f"Hello {x.username}, a new article has been added to the Students Projects Share App.\n \n Please visit our application to see more. \n \n Click on the link below to be the first. \n https://play.google.com/store/apps/details?id=ttpc.StudentsProjectsShare"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=True)
            
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateNewExpert(APIView):
    def post(self, request, format=None):
        serializer = ExpertsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            #Send message to all user when new data is added
            queryset = MyUser.objects.all()
            for x in queryset:
                # Send an email to the user
                email = x.email
                subject = "Students Projects Share"
                message = f"Hello {x.username}, a new Expert has been added to the Students Projects Share App.\n \n Please visit our application to see more. \n \n Click on the link below to be the first. \n https://play.google.com/store/apps/details?id=ttpc.StudentsProjectsShare"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class CreateNewWork(APIView):
    def post(self, request, format=None):
        serializer = PeopleWorksSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()

            #Send message to all user when new data is added
            queryset = MyUser.objects.all()
            for x in queryset:
                # Send an email to the user
                email = x.email
                subject = "Students Projects Share"
                message = f"Hello {x.username}, a new work has been added to the Students Projects Share App.\n \n Please visit our application to see more. \n \n Click on the link below to be the first. \n https://play.google.com/store/apps/details?id=ttpc.StudentsProjectsShare"
                from_email = settings.EMAIL_HOST_USER
                recipient_list = [email]
                send_mail(subject, message, from_email, recipient_list, fail_silently=True)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
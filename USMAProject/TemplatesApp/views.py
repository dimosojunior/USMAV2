from django.shortcuts import render,redirect
from USMAApp.models import *
from django.http import JsonResponse
from django.db.models import Q
from TemplatesApp.forms import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def USMAHome(request):

	return render(request, 'TemplatesApp/home.html')


def UniversitiesView(request):
	universities = Universities.objects.all().order_by('?')
	# form ya kusearch
	form = UniversitySearchForm(request.POST or None)
	if request.method =="POST":
		universities = Universities.objects.filter(UniversityName__icontains=form['UniversityName'].value())


	context = {
		"universities":universities,
		"form":form,
	}

	return render(request, 'TemplatesApp/Universities.html',context)




#--------------------------------COURSES--------------------


#---------------------------------------COURSES-------------
def AllUniversityCourses(request,id):
	UniversityId = Universities.objects.get(id=id)
	university_name = UniversityId.UniversityName
	university_id = UniversityId.id

	request.session['university_id'] = university_id

	courses = UniversityCourses.objects.filter(
			university__id__icontains = UniversityId.id
		).order_by('?')

	# form ya kusearch
	form = SearchCourseForm(request.POST or None)
	if request.method =="POST":
		courses = UniversityCourses.objects.filter(CourseName__icontains=form['CourseName'].value())


	context = {
		"courses":courses,
		"form":form,
		"university_name":university_name,
	}

	return render(request, 'TemplatesApp/UniversityCourses.html',context)















#----------------------PROJECTS-----------------------------



#---------------------- PROJECTS----------------------


#----------------------- PROJECTS--------


def AllUniversityProjects(request,id):
	CourseId = UniversityCourses.objects.get(id=id)
	CourseId_name = CourseId.CourseName
	university_id = request.session.get('university_id', '')
	print(f"UNI ID {university_id}")

	projects = AllProjects.objects.filter(
		university__id__icontains = university_id, 
		CourseName__CourseName__icontains = CourseId_name
		)
	
	# form ya kusearch
	form = ProjectSearchForm(request.POST or None)
	if request.method =="POST":
		projects = AllProjects.objects.filter(
			university__id__icontains = university_id, 
			CourseName__CourseName__icontains = CourseId_name,
			ProjectName__icontains=form['ProjectName'].value())


	context = {
		"projects":projects,
		"form":form,
		"CourseId_name":CourseId_name,
	}

	return render(request, 'TemplatesApp/AllProjects.html',context)














#----------------------------READ PROJECT------------------

def ReadProject(request,id):
	ReadProject = AllProjects.objects.get(id=id)

	context = {
		"ReadProject":ReadProject,
	}

	return render(request, 'TemplatesApp/ReadProject.html',context)















#-------------------------------HOB------------------------------


def HobsView(request):
	hobs = Hob.objects.all().order_by('?')

	form = HobSearchForm(request.POST or None)
	if request.method =="POST":
		hobs = Hob.objects.filter(CategoryName__icontains=form['CategoryName'].value())


	context = {
		"hobs":hobs,
		"form":form,
	}

	return render(request, 'TemplatesApp/HOB/HobsView.html',context)




# -------------------ALL EXPERTS-------------
def AllExperts(request, id):
	hobId = Hob.objects.get(id=id)
	hobId_name = hobId.CategoryName
	experts = Experts.objects.filter(
		CategoryName__id__icontains = hobId.id
		).order_by('?')
	# form ya kusearch
	form = ExpertsSearchForm(request.POST or None)
	if request.method =="POST":
		experts = Experts.objects.filter(
			CategoryName__id__icontains = hobId.id, 
			StudentName__icontains=form['StudentName'].value())


	context = {
		"experts":experts,
		"form":form,
		"hobId_name":hobId_name,
	}

	return render(request, 'TemplatesApp/AllExperts.html',context)








#----------------------------READ EXPERT------------------

def ReadExpert(request,id):
	ReadExpert = Experts.objects.get(id=id)

	context = {
		"ReadExpert":ReadExpert,
	}

	return render(request, 'TemplatesApp/ReadExpert.html',context)












#---------------------------ARTICLES-------------------------------




# ------------------- ALL ARTICLES-------------
def ArticlesView(request):
	articles = Articles.objects.all().order_by('?')
	# form ya kusearch
	form = ArticleSearchForm(request.POST or None)
	if request.method =="POST":
		articles = Articles.objects.filter(ArticlesName__icontains=form['ArticlesName'].value())


	context = {
		"articles":articles,
		"form":form,
	}

	return render(request, 'TemplatesApp/ARTICLES/ArticlesView.html',context)


# ------------------- ALL ARTICLES-------------
def AllArticles(request,id):
	articleId = Articles.objects.get(id=id)
	articleId_name = articleId.ArticlesName
	articles = ArticlesCategory.objects.filter(
		ArticlesName__id__icontains = articleId.id
		).order_by('?')

	# form ya kusearch
	form = ArticleCategorySearchForm(request.POST or None)
	if request.method =="POST":
		articles = ArticlesCategory.objects.filter(
			ArticlesName__id__icontains = articleId.id,
			Title__icontains=form['Title'].value())


	context = {
		"articles":articles,
		"form":form,
		"articleId_name":articleId_name,
	}

	return render(request, 'TemplatesApp/AllArticles.html',context)









#----------------------------READ EXPERT------------------

def ReadArticle(request,id):
	ReadArticle = ArticlesCategory.objects.get(id=id)

	context = {
		"ReadArticle":ReadArticle,
	}

	return render(request, 'TemplatesApp/ReadArticle.html',context)


















def search_university_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(UniversityName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    university = Universities.objects.filter(search)
    mylist= []
    mylist += [x.UniversityName for x in university]
    return JsonResponse(mylist, safe=False)

#SEARCH UNIVERSITY COURSE
def search_university_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(CourseName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    course = UniversityCourses.objects.filter(search)
    mylist= []
    mylist += [x.CourseName for x in course]
    return JsonResponse(mylist, safe=False)









#-----------------------PROJECT SEARCH------------------

def project_search_university_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(ProjectName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    project = AllProjects.objects.filter(search)
    mylist= []
    mylist += [x.ProjectName for x in project]
    return JsonResponse(mylist, safe=False)




#-----------------------HOB SEARCH------------------

def search_hob_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(CategoryName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    hob = Hob.objects.filter(search)
    mylist= []
    mylist += [x.CategoryName for x in hob]
    return JsonResponse(mylist, safe=False)






#---------------------------SEARCH EXPERTS----------------------






#----------------------- SEARCH WEBSITES EXPERTS------------------
def experts_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(StudentName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    expert = Experts.objects.filter(search)
    mylist= []
    mylist += [x.StudentName for x in expert]
    return JsonResponse(mylist, safe=False)





















#--------------------------------SEARCH ARTICLE--------------------



def all_articles_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(ArticlesName__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    article = Articles.objects.filter(search)
    mylist= []
    mylist += [x.ArticlesName for x in article]
    return JsonResponse(mylist, safe=False)


def articles_search_autocomplete(request):
    print(request.GET)
    #form = AvailableMedicinesForm()
    query_original = request.GET.get('term')
    search = Q(Title__icontains=query_original)
    #queryset = Dozi.objects.filter(name__icontains=query_original)
    article = ArticlesCategory.objects.filter(search)
    mylist= []
    mylist += [x.Title for x in article]
    return JsonResponse(mylist, safe=False)





















#------------------------ADD PROJECT------------------










#---------------------------MUST------------------------------


def AddProject(request):
	form = AddProjectForm()


	if request.method == "POST":
		ProjectName = request.POST.get('ProjectName')
		form = AddProjectForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"{ProjectName} Added Successfuly")
			return redirect('AddProject')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddProject')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddProject/AddProject.html',context)
























#--------------------------------ADD ARTICES-------------------------------------




def AddArtcle(request):
	form = AddArtcleForm()


	if request.method == "POST":
		Title = request.POST.get('Title')
		form = AddArtcleForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()
			messages.success(request, f"Article: {Title}, Added Successfuly")
			return redirect('AddArtcle')

		messages.info(request, "There is a problem when you are creating a new project")
		return redirect('AddArtcle')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/AddArticle/AddArtcle.html',context)




def AddExpert(request):
    form = AddExpertsForm()


    if request.method == "POST":
        #Title = request.POST.get('Title')
        form = AddExpertsForm(request.POST or None, files=request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, f"Data is added Successfuly")
            return redirect('AddExpert')

        messages.info(request, "There is a problem when you are creating a new project")
        return redirect('AddExpert')


    context = {
        "form":form,
    }

    return render(request, 'TemplatesApp/AddExpert.html',context)





#--------------------CONTACT ME----------------------------

def ContactMe(request):
	form = ContactMeForm()


	if request.method == "POST":
		FullName = request.POST.get('FullName')
		Email = request.POST.get('Email')
		Message = request.POST.get('Message')
		MyEmail = "juniordimoso8@gmail.com"

		form = ContactMeForm(request.POST or None, files=request.FILES)
		if form.is_valid():
			form.save()

			#HIZI NI KWA AJILI KUTUMA EMAIL KWENDA KWA USER
            
			subject = "University Students Materials App"
			message = f"Ahsante  {FullName} Ahsante Kwa kutembelea Kwenye Mfumo Wetu"
			from_email = settings.EMAIL_HOST_USER
			recipient_list = [Email]
			send_mail(subject, message, from_email, recipient_list, fail_silently=True)

			#HIZI NI KWA AJILI KUTUMA EMAIL KWENDA KWA ADMIN

			subject2 = "University Students Materials App"
			message2 = f"  {Message} "
			from_email2 = settings.EMAIL_HOST_USER
			recipient_list2 = [MyEmail]
			send_mail(subject2, message2, from_email2, recipient_list2, fail_silently=True)




			messages.success(request, f"Hey: {FullName}, Your Message Sent Successfuly")
			return redirect('ContactMe')

		messages.info(request, "There is a problem when you are Sending a new project")
		return redirect('ContactMe')


	context = {
		"form":form,
	}

	return render(request, 'TemplatesApp/ContactMe.html',context)

from USMAApp.models import *
from django.forms import ModelForm
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate


class UniversitySearchForm(forms.ModelForm):
	
	UniversityName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'university', 'placeholder' : 'Search University'})

	)
	
	class Meta:
		model = Universities
		fields =['UniversityName']

#SEARCH COURSE
class SearchCourseForm(forms.ModelForm):
	
	CourseName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'course', 'placeholder' : 'Search Course'})

	)
	
	class Meta:
		model = UniversityCourses
		fields =['CourseName']






class HobSearchForm(forms.ModelForm):
	
	CategoryName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'hob', 'placeholder' : 'Search Expert Category'})

	)
	
	class Meta:
		model = Hob
		fields =['CategoryName']





#-------------------------------SEARCH EXPERT----------------------------

class ExpertsSearchForm(forms.ModelForm):
	
	StudentName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'expert', 'placeholder' : 'Search Expert'})

	)
	
	class Meta:
		model = Experts
		fields =['StudentName']






#---------------------------MWISHO WA EXPERTS SEARCH FORM--------------




#-------------------------------SEARCH ARTICLE----------------------------

class ArticleSearchForm(forms.ModelForm):
	
	ArticlesName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'article', 'placeholder' : 'Search Article'})

	)
	
	class Meta:
		model = Articles
		fields =['ArticlesName']


class ArticleCategorySearchForm(forms.ModelForm):
	
	Title = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'article', 'placeholder' : 'Search Article'})

	)
	
	class Meta:
		model = ArticlesCategory
		fields =['Title']





















#---------------------------PROJECTS FORM-------------------


class ProjectSearchForm(forms.ModelForm):
	
	ProjectName = forms.CharField(
		required=True,
	#label=False,
		widget=forms.TextInput(attrs={'id' :'project', 'placeholder' : 'Search Project'})

	)
	
	class Meta:
		model = AllProjects
		fields =['ProjectName']





#---------------------------ADD PROJECTS FORMS-------------------


class AddProjectForm(forms.ModelForm):
	
	class Meta:
		model = AllProjects
		fields ='__all__'
		#fields= ["university","ProjectName", "StudentName", "CourseName","Year"]




#------------------------ADD ARTICLE------------------

class AddArtcleForm(forms.ModelForm):
	
	class Meta:
		model = ArticlesCategory
		fields ='__all__'
		#fields= ["university","ProjectName", "StudentName", "CourseName","Year


#------------------------ADD ARTICLE------------------

class AddExpertsForm(forms.ModelForm):
	
	class Meta:
		model = Experts
		fields ='__all__'
		#fields= ["university","ProjectName", "StudentName", "CourseName","Year







class ContactMeForm(forms.ModelForm):
	
	class Meta:
		model = ContactMe
		fields ='__all__'
		#fields= ["university","ProjectName", "StudentName", "CourseName","Year"]

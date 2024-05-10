
from django.urls import path
from . import views


urlpatterns = [
    path('', views.USMAHome, name="USMAHome"),
    path('Universities/', views.UniversitiesView, name="Universities"),



#-------------------------ALL COURSES---------------------------
    path('AllUniversityCourses/<int:id>/', views.AllUniversityCourses, name="AllUniversityCourses"),


   #-------------------------ALL PROJECTS---------------------------
    
    path('AllUniversityProjects/<int:id>/', views.AllUniversityProjects, name="AllUniversityProjects"),
    













#----------------------READ PROJECT-------------------------
    path('ReadProject/<int:id>/', views.ReadProject, name="ReadProject"),











#-----------------------------HOB----------------------------------



	path('Hob/', views.HobsView, name="HobsView"),


	path('AllExperts/<int:id>/', views.AllExperts, name="AllExperts"),
	

 






 #----------------------------ARTICLES----------------------------



 	path('Articles/', views.ArticlesView, name="ArticlesView"),

 	path('AllArticles/<int:id>/', views.AllArticles, name="AllArticles"),
 	




#--------------------------READ ARTICLE----------------------

	path('ReadArticle/<int:id>/', views.ReadArticle, name="ReadArticle"),









#--------------------------ADD ARTICLES----------------------------------------
	path('AddArtcle/', views.AddArtcle, name="AddArtcle"),
	











#----------------------------SEARCH-----------------------------
 	path('search_university_autocomplete/', views.search_university_autocomplete, name="search_university_autocomplete"),


#-------------------------------SEARCH COURSES-------------------
 	path('search_university_autocomplete/', views.search_university_autocomplete, name="search_university_autocomplete"),
 	



#------------------------SEARCH PROJECT-------------------------
	path('project_search_university_autocomplete/', views.project_search_university_autocomplete, name="project_search_university_autocomplete"),


#------------------------SEARCH HOB-------------------------
	path('search_hob_autocomplete/', views.search_hob_autocomplete, name="search_hob_autocomplete"),


#------------------------SEARCH EXPERTS-------------------------
	path('experts_search_autocomplete/', views.experts_search_autocomplete, name="experts_search_autocomplete"),
	






#------------------------SEARCH ARTICLES-------------------------
	path('all_articles_search_autocomplete/', views.all_articles_search_autocomplete, name="all_articles_search_autocomplete"),

	path('articles_search_autocomplete/', views.articles_search_autocomplete, name="articles_search_autocomplete"),
	








#------------------CONTACT ME----------------------------
	path('ContactMe/', views.ContactMe, name="ContactMe"),








#----------------------------------READ EXPERT---------------------------
	path('ReadExpert/<int:id>/', views.ReadExpert, name="ReadExpert"),



#-------------------------------ADD PROJECT------------------------


#---------------------------ADD PROJECT-----------------------------
	path('AddProject/', views.AddProject, name="AddProject"),
	path('AddExpert/', views.AddExpert, name="AddExpert"),
	


]

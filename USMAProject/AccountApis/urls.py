from . import views
from django.urls import path


urlpatterns = [
	path('signin/', views.signin, name="signin"),
	path('signup/', views.signup, name="signup"),
    path('logout/', views.logout, name='logout'),

    

    #---------------KWA AJILI YA APIS --------------
    path('register_user/', views.RegistrationView.as_view(), name='register2'),
    path('login_user/', views.ReactLoginView.as_view(), name='login2'),
    path('logout_user/', views.LogoutView.as_view(), name='logout2'),
    path('user_data/', views.UserDataView.as_view(), name='user-data2'),
    
    # path('UserView/', views.UserView.as_view(), name="UserView"),

     
]
from django.contrib import admin

from django.urls import path
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static

from.import views

urlpatterns = [
    # post views
    path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('', views.dashboard, name='dashboard'),
    path('password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
	path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
	path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
	path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
	path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
	path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
	path('register/', views.register, name='register'),
	# path('', views.index),
	path('account/home/', views.index, name='home'),
	path('categories/', views.categories, name='categories' ),
	#path('home/', views.categories ),       
	path('restaurants/', views.restaurants),    
	path('choices/', views.getChoices, name='choices'),
	path('admin/', admin.site.urls),
    # path('account/', views.categories),     
]


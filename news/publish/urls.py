
from . import views

from django.urls import path, include


#if settings.DEBUG:
 #       urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

urlpatterns = [

path('', views.index, name = 'index'),
path('edit/', views.edit, name='edit'),
path('dater/', views.current_datetime, name='current_datetime'),
path('dater/plus/<int:offset>', views.timeahead, name='timeahead'  ),
path('search-form/', views.search_form, name='search_form'),
path('search/', views.search, name='search'),
path('add-book/', views.register, name='register'),
path('submit/', views.submit, name='submit'),
path('delete/', views.delete, name='delete'),
path('login/', views.loginpage, name='loginpage'),
path('login-status/', views.login, name='login'),
path('upload/', views.picture, name='picture'),
path('contact/', views.contact, name='contact'),
path('pictures/', views.picture_status, name='picture_status'),
path('edit_save/', views.edit_save, name='edit_save'),
path('sign_up/', views.signup, name='signup'),
]




"""student_management_system URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from . import views,Hod_Views,Staff_Views,Student_Views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/',views.BASE,name='base'),

    # LOGIN
    path('',views.LOGIN,name='login'),
    path('dologin',views.dologin,name='dologin'),
    path('dologout',views.dologout,name='logout'),

    # profile update
    path('profile',views.PROFILE,name='profile'),
    path('profile/update',views.PROFILE_UPDATE,name='profile_update'),


    # HOD PANEL
    path('HoD/home/',Hod_Views.HOME,name='hod_home'),
    path('HoD/student/add/',Hod_Views.ADD_STUDENT,name='add_student'),
    path('HoD/student/view',Hod_Views.VIEW_STUDENT,name='view_student'),
    path('HoD/student/edit/<str:id>', Hod_Views.EDIT_STUDENT, name='edit_student'),
    path('HoD/student/update', Hod_Views.UPDATE_STUDENT, name='update_student'),
    path('HoD/student/delete/<str:admin>', Hod_Views.DELETE_STUDENT, name='delete_student'),


    path('HoD/staff/add',Hod_Views.ADD_STAFF,name='add_staff'),
    path('HoD/staff/view',Hod_Views.VIEW_STAFF,name='view_staff'),
    path('HoD/staff/edit/<str:id>',Hod_Views.EDIT_STAFF,name='edit_staff'),
    path('HoD/staff/update',Hod_Views.UPDATE_STAFF,name='update_staff'),
    path('HoD/staff/delete/<str:id>',Hod_Views.DELETE_STAFF,name='delete_staff'),


    path('HoD/subject/add',Hod_Views.ADD_SUBJECT,name='add_subject'),
    path('HoD/subject/view',Hod_Views.VIEW_SUBJECT,name='view_subject'),
    path('HoD/subject/edit/<str:id>',Hod_Views.EDIT_SUBJECT,name='edit_subject'),
    path('HoD/subject/update',Hod_Views.UPDATE_SUBJECT,name='update_subject'),
    path('HoD/subject/delete/<str:id>',Hod_Views.DELETE_SUBJECT,name='delete_subject'),


    path('HoD/session/add',Hod_Views.ADD_SESSION,name='add_session'),
    path('HoD/session/view',Hod_Views.VIEW_SESSION,name='view_session'),
    path('HoD/session/edit/<str:id>',Hod_Views.EDIT_SESSION,name='edit_session'),
    path('HoD/session/update',Hod_Views.UPDATE_SESSION,name='update_session'),
    path('HoD/session/delete/<str:id>',Hod_Views.DELETE_SESSION,name='delete_session'),



    path('HoD/course/add',Hod_Views.ADD_COURSE,name='add_course'),
    path('HoD/course/view',Hod_Views.VIEW_COURSE,name='view_course'),
    path('HoD/course/edit/<str:id>',Hod_Views.EDIT_COURSE,name='edit_course'),
    path('HoD/course/update',Hod_Views.UPDATE_COURSE,name='update_course'),
    path('HoD/course/delete/<str:id>', Hod_Views.DELETE_COURSE, name='delete_course'),




#     STAFF PANEL
    path('Staff/home',Staff_Views.HOME,name='staff_home'),


] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)

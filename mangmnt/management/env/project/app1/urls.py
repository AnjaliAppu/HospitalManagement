"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from. import views

urlpatterns = [

    path('index', views.index, name='index'),

    path('home', views.home, name='home'),
    path('PatientRegistration', views.PatientRegistration, name='PatientRegistration'),
    path('viewpatient', views.viewpatient, name='viewpatient'),
    path('editpatient/<int:id>', views.editpatient, name='editpatient'),
    path('updatepatient/<int:id>', views.updatepatient, name='updatepatient'),
    path('deletepatient/<int:id>', views.deletepatient, name='deletepatient'),
    path('DoctorRegistration',views.DoctorRegistration,name='DoctorRegistration'),
    path('viewdoctor',views.viewdoctor,name='viewdoctor'),
    path('editdoctor/<int:id>', views.editdoctor, name='editdoctor'),
    path('updatedoctor/<int:id>', views.updatedoctor, name='updatedoctor'),
    path('deletedoctor/<int:id>', views.deletedoctor, name='deletedoctor'),
    path('gallery',views.gallery,name='gallery'),
    path('appointment',views.appointment,name='appointment'),
    path('viewappointment',views.viewappointment,name='viewappointment'),
    path('editappointment/<int:id>', views.editappointment, name='editappointment'),
    path('updateappointment/<int:id>', views.updateappointment, name='updateappointment'),
    path('deleteappointment/<int:id>', views.deleteappointment, name='deleteappointment'),
    path('about',views.about,name='about'),
    path('viewlogin',views.viewlogin,name='viewlogin'),
    path('Addmaster',views.Addmaster,name='Addmaster'),
    path('Signup',views.Signup,name='Signup'),
    path('LoginFrm',views.LoginFrm,name='LoginFrm'),
    path('', views.Newaccount,name='Newaccount'),
    path('UserModule', views.UserModule,name='UserModule'),
    path('Department', views.Department,name='Department'),
    path('viewdepartment', views.viewdepartment,name='viewdepartment'),
    path('DoctorModule', views.DoctorModule, name='DoctorModule'),
    path('Disease', views.Disease, name='Disease'),
    path('viewdisease', views.viewdisease, name='viewdisease'),
    path('myappointmentview', views.myappointmentview, name='myappointmentview'),
    path('specialitydoctors', views.specialitydoctors, name='specialitydoctors'),
    path('PatientEnquiry', views.PatientEnquiry, name='PatientEnquiry'),
    path('viewEnquiry', views.viewEnquiry, name='viewEnquiry'),
    path('viewapproved', views.viewapproved, name='viewapproved'),
    path('Approveappointment', views.Approveappointment,name='Approveappointment'),
    path('ApproveADMIN', views.ApproveADMIN, name='ApproveADMIN'),









]

from django.shortcuts import render, redirect
from .models import Patient,Doctor,PatientAppointment,Login,AdminMaster,Masteraccount,DepartmentSection,DiseaseList
from .forms import PatientForm, DoctorForm, AppointmentForm, LoginForm, MasterForm,AccountForm,DepartmentForm,DiseaseForm

# Create your views here.
def index(request):
    return render(request, 'index.html')
def home(request):
    return render(request, 'home.html')


def PatientRegistration(request):

    if request.method=="POST":
        form=PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=PatientForm()
    return render(request,'PatientRegistration.html')

def viewpatient(request):
    result = Patient.objects.all()
    return render(request,'viewpatient.html', {'result': result})
def editpatient(request,id):
    result = Patient.objects.get(id=id)
    return render(request,'editpatient.html', {'result': result})

def deletepatient(request,id):
    result=Patient.objects.get(id=id)
    result.delete()
    return redirect('/viewpatient')


def updatepatient(request, id):
    result=Patient.objects.get(id=id)
    form=PatientForm(request.POST, instance=result)
    if form.is_valid():
        form.save()
        return redirect('/viewpatient')
    return render(request, 'editpatient.html', {'result': result})


def DoctorRegistration(request):
    if request.method == "POST":
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/viewdoctor")
    else:
        form = DoctorForm()
    return render(request, 'DoctorRegistration.html')

def viewdoctor(request):
    result=Doctor.objects.all()
    return render(request,'viewdoctor.html',{'result':result})

def editdoctor(request,id):
    result = Doctor.objects.get(id=id)
    return render(request,'editdoctor.html', {'result': result})

def deletedoctor(request,id):
    result=Doctor.objects.get(id=id)
    result.delete()
    return redirect('/viewdoctor')


def updatedoctor(request,id):
    result=Doctor.objects.get(id=id)
    form=DoctorForm(request.POST, instance=result)
    if form.is_valid():
        form.save()
        return redirect('/viewdoctor')
    return render(request, 'editdoctor.html', {'result': result})






def about(request):
    return render(request, 'about.html')
def gallery(request):
    return render(request,'gallery.html')

def appointment(request):
    if request.method=="POST":
            form=AppointmentForm(request.POST)
            if form.is_valid():
                form.save()
                return render(request,'home.html')
    else:
        form=AppointmentForm()
    return render(request,'appointment.html')

def viewappointment(request):
    result = PatientAppointment.objects.all()
    return render(request,'viewappointment.html', {'result': result})

def editappointment(request,id):
    result = PatientAppointment.objects.get(id=id)
    return render(request,'editappointment.html', {'result': result})

def deleteappointment(request,id):
    result=PatientAppointment.objects.get(id=id)
    result.delete()
    return redirect('/viewappointment')


def updateappointment(request,id):
    result=PatientAppointment.objects.get(id=id)
    form=AppointmentForm(request.POST, instance=result)
    if form.is_valid():
        form.save()
        return redirect('/viewappointment')
    return render(request, 'editappointment.html', {'result': result})


def LoginFrm(request):
    if request.method=="POST":
        form=LoginForm(request.POST)
        if form.is_valid():
            username=form['username'].valid()
            password=form['password'].valid()
            try:
                user=Login.objects.get(username=username,password=password)
                if user is not None:
                    return render(request,'home.html')
            except:
               pass
    else:
        return render(request, 'LoginFrm.html')



def Signup(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        try:
            user=Patient.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'UserModule.html')
            return render(request, 'Signup.html')
        except:
             pass
        try:
           user=Login.objects.get(username=username,password=password)
           if user is not None:
               print(user)
               return render(request, 'home.html')
        except:
            pass

        try:
            user=Doctor.objects.get(username=username,password=password)
            if user is not None:
                print(user)
                return render(request,'DoctorModule.html')
            return render(request,'Signup.html')
        except:
             pass
    else:
        return render(request,'Signup.html')



def viewlogin(request):
    result = Login.objects.all()
    return render(request, 'viewlogin.html',{'result': result})

def Addmaster(request):
    if request.method =="POST":
        form = MasterForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form = MasterForm()
    return render(request,'Addmaster.html')

def UserPatient(request):
    return render(request,'Userpatient.html')

def Department(request):
    if request.method == "POST":
        form = DepartmentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form = DepartmentForm()
    return render(request,'Department.html')

def viewdepartment(request):
    return render(request,'viewdepartment.html')


def Newaccount(request):
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/home")
    else:
        form = AccountForm()
    return render(request,'Newaccount.html')

def UserModule(request):
    return render(request,'UserModule.html')
def DoctorModule(request):
    return render(request,'DoctorModule.html')

def Disease(request):
    if request.method=="POST":
        form=DiseaseForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=DiseaseForm()
    return render(request,'Disease.html')

def viewdisease(request):
    result = DiseaseList.objects.all()
    return render(request,'viewdisease.html',{'result':result})
def myappointmentview(request):
    result =PatientAppointment.objects.filter()
    return render(request,'myappointmentview.html')
def specialitydoctors(request):
    return render(request,'specialitydoctors.html')

def PatientEnquiry(request):
    if request.method=="POST":
        form=PatientAppointment(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        form=DiseaseForm()
        return render(request,'PatientEnquiry.html')
def viewEnquiry(request):
    result = PatientAppointment.objects.all()
    return render(request,'viewEnquiry.html')
def viewapproved(request):
    result =PatientAppointment.objects.all()
    return render(request,'viewapproved.html')
def Approveappointment(request):
    return render(request,'Approveappointment.html')
def ApproveADMIN(request):
    return render(request,'ApproveADMIN.html')









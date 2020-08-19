import os
from django.shortcuts import render
from .models import query_students
from django.core.files.storage import FileSystemStorage
from django.templatetags.static import static
from django.conf import settings
# Create your views here.
def dashboard(request):
    return render(request, 'pmf/dashboard.html')
    
def download(request):
    path = settings.MEDIA_ROOT
    file_list = os.listdir(path)
    context = {'files':file_list}
    return render(request, 'pmf/download.html', context)



def index(request):
    return render(request, 'pmf/index.html')



def list(request):
    data = query_students.objects.all()
    list_data = {'web_data' : data}
    return render(request, 'pmf/list.html',list_data)

def query(request):
    if request.method == 'POST':
        email = request.POST['email']
        name = request.POST['name']
        phone = request.POST['phone']
        query_student = query_students(email=email,phone=phone,name=name)
        query_student.save()

    return render(request, 'pmf/query.html')
    
    
    
def test_upload(request):
    if request.method == 'POST' and request.FILES['myfile']:
        myfile = request.FILES['myfile']
        fs=FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)
        return render(request, 'pmf/test_upload.html', {
            'uploaded_file_url': uploaded_file_url
        })
    return render(request, 'pmf/test_upload.html')
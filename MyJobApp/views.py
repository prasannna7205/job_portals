from django.shortcuts import render,HttpResponse
from rest_framework import response
from MyJobApp.models import Student,JobTable
from django.shortcuts import render, get_object_or_404
from django.views import View
from django.contrib.auth.models import User
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from django.contrib.auth import login,authenticate
from rest_framework.pagination import PageNumberPagination
from MyJobApp.serializers import JobTableSerializer
from django.views.generic import ListView
# Create your views here.
def Homepage(request):
    return render ( request, 'index.html')
# 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
# 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
@csrf_exempt 
def UserInformation(request):
    if request.method == "POST":
        email=request.POST['email']
        pass1=request.POST['password']
        pass2=request.POST['comformpassword']
        if pass1!=pass2:
            data={"massege:registation faild "}
            return JsonResponse(data,status=400)
        else:
            user =User.objects.create_user(email,pass1,pass2)
            user.save()
            response_data = {'message': 'Form data received successfully'}
            return JsonResponse(response_data, status=200)
        
@csrf_exempt     
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            senddata = {'message': 'You have successfully logged in. Welcome to the home page.'}
            return JsonResponse(senddata, status=200)
        else:
            return JsonResponse({'message': 'Your email or password is wrong'}, status=400)



from django.views.generic import ListView
from .models import JobTable

class JobListView(View):
    template_name = 'jobpost/jobpost.html'
    def get(self, request):
        jobs = JobTable.objects.all()
        return render(request, self.template_name, {'jobs': jobs})


 
class JobDetailView(View):
    template_name = 'job_details/job_detail.html'

    def get(self, request, job_id):
        job = get_object_or_404(JobTable, pk=job_id)
        return render(request, self.template_name, {'job': job})







# import os
# from django.shortcuts import render
# from django.core.files import File
# from faker import Faker
# from .models import JobTable

# def generate_fake_data(request):
#     fake = Faker()
#     for _ in range(10):  # Generate data for 10 job entries (you can change the number as needed)
#         jobname = fake.job()
#         image_filepath = 'media\job_images'  # Replace with the full image file path
#         postdescription = fake.text()
#         people_required = fake.random_int(min=1, max=100)
#         job_type = fake.word()
#         salary = fake.random_int(min=20000, max=100000)  # Adjust salary range as needed

#         # Create a JobTable instance with the image
#         job = JobTable(
#             jobname=jobname,
#             postdescription=postdescription,
#             people_required=people_required,
#             job_type=job_type,
#             salary=salary
#         )

#         # Open the image file and assign it to the image field
#         with open(image_filepath, 'rb') as f:
#             job.image.save(os.path.basename(image_filepath), File(f))

#         job.save()

#     return render(request, 'success_template.html')






# from django.contrib.auth import login, authenticate
# from django.contrib.auth.forms import UserCreationForm
# from django.shortcuts import render, redirect
# from django.views import View
# from django.http import JsonResponse

# class RegisterView(View):
#     def get(self, request):
#         # Render the registration form
#         return render(request, 'registration/register.html')

#     def post(self, request):
#         # Process the registration form submission
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             login(request, user)
#             return JsonResponse({'message': 'Registration successful'}, status=200)
#         else:
#             errors = form.errors
#             return JsonResponse(errors, status=400)

# class LoginView(View):
#     def get(self, request):
#         # Render the login form
#         return render(request, 'registration/login.html')

#     def post(self, request):
#         # Process the login form submission
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return JsonResponse({'message': 'Login successful'}, status=200)
#         else:
#             return JsonResponse({'message': 'Login failed. Check your credentials.'}, status=400)


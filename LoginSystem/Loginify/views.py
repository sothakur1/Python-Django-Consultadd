from django.http import HttpResponse
# Create your views here.
from .models import UserDetails
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

def LoginifyView(request):
    return HttpResponse("Hellow, World!!")

def signup(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        
        if UserDetails.objects.filter(email = email).exists():
            messages.error(request, 'Email already signuped')
            return redirect('signup')
    
        UserDetails.objects.create(username= username, email= email, password =password)
        messages.success(request, 'Signup sucesssful.')
        return redirect('login')

    return render(request, 'signup.html')

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = UserDetails.objects.get(email=email, password=password)
            return render(request, 'success.html', {'username': user.username})
        except UserDetails.DoesNotExist:
            messages.error(request, 'Invalid credentials')
            return redirect('login')

    return render(request, 'login.html')

def get_all_users(request):
    users = UserDetails.objects.all().values('username', 'email')
    return JsonResponse(list(users), safe=False)
        
def getUser_by_email(request,email):
    try:
        user = UserDetails.objects.get(email=email)
        data = {
            'username': user.username,
            'email': user.email
        }
        return JsonResponse(data)
    except UserDetails.DoesNotExist:
        return JsonResponse({'error': 'User not found'}, status=404)

@csrf_exempt
def update_user(request, email):
    if request.method == 'POST':
        try:
            user = UserDetails.objects.get(email=email)
            data = json.loads(request.body)

            username = data.get('username')
            password = data.get('password')

            if username:
                user.username = username
            if password:
                user.password = password

            user.save()
            return JsonResponse({'message': 'User updated successfully'})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found'}, status=404)
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON'}, status=400)

    return JsonResponse({'error': 'Invalid request method'}, status=405)

@csrf_exempt
def delete_user(request, email):
    if request.method == 'DELETE':
        try:
            user = UserDetails.objects.get(email=email)
            user.delete()
            return JsonResponse({'message': 'User deleted successfully'})
        except UserDetails.DoesNotExist:
            return JsonResponse({'error': 'User not found, Please try with corret user'}, status=404)

    return JsonResponse({'error': 'Invalid request method'}, status=405)
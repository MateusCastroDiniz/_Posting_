from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from django.contrib import messages
from ..models.user import User

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed')  # Redireciona para a página de feed
        else:
            messages.error(request, "Credenciais inválidas. Por favor, tente novamente.")
            return render(request, 'login.html')
    else:
        return render(request, 'login.html')
    # if request.method == 'GET':
    #     return render(request, 'login.html')
    # else:
    #     email = request.POST.get('email')
    #     password = request.POST.get('password')
    #
    #     user = authenticate(request, email=email, password=password)
    #
    #     if user:
    #         login(request, user)
    #         return redirect('feed')  # Redireciona para a página de feed
    #     else:
    #         messages.error(request, f"Credenciais inválidas. Por favor, tente novamente.")
    #         return render(request, 'login.html')




#
# def register_view(request):

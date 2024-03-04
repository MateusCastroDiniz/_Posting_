from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

def login_view(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('feed.html')
        else:
            # Credenciais inválidas, exibir mensagem de erro no template
            error_message = "Credenciais inválidas. Por favor, tente novamente."
            return render(request, 'login.html', {'error_message': error_message})
    else:
        return render(request, 'login.html')


def user_info(request):
    user = request.user

    context = {
        'user_info': {
            'first_name': user.username
            'email':
        }
    }
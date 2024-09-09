from django.contrib.auth import authenticate, login
from django.shortcuts import render


# view que renderiza index.html
def index(request):
    if request.method == 'POST':
        username = request.POST['username'].strip()
        password = request.POST['password'].strip()
        user = authenticate(request, username=username, password=password)
        if user is None:
            context = {
                'alerta': 'Usuário ou senha incorreta'
            }
            return render(request, 'index.html', context)
        else:
            login(request, user)
    return render(request, 'index.html')

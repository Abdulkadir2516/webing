from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from .forms import RegisterForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages  # hata mesajları için
from .forms import AddWordForm  # Bunu oluşturacağız

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('home')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})


@login_required
def home(request):
    # Örnek değerler, gerçek veritabanından çekebilirsin
    daily_goal = 20
    repeated_words_today = 12
    repeat_data = [5, 8, 10, 7, 12, 15, 12]  # Hafta içi günlük tekrarlar

    # Kelime ekleme formu (modal için)
    add_word_form = AddWordForm()

    context = {
        'daily_goal': daily_goal,
        'repeated_words_today': repeated_words_today,
        'repeat_data': repeat_data,
        'add_word_form': add_word_form,
    }
    return render(request, 'home.html', context)

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        print(user)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Kullanıcı adı veya şifre yanlış')
    return render(request, 'login.html')


@login_required
def add_word(request):
    if request.method == 'POST':
        form = AddWordForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')  # veya başka bir sayfa
    else:
        form = AddWordForm()
    return render(request, 'add_word.html', {'form': form})
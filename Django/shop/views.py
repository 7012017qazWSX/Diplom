from django.shortcuts import render, redirect, get_object_or_404
from .models import Book, Cart
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

def home(request):
    return render(request, 'home.html')

def shop_view(request):
    books = Book.objects.all()
    return render(request, 'shop.html', {'books': books})

def add_to_cart(request, book_id):
    if not request.user.is_authenticated:
        return redirect('login')
    book = get_object_or_404(Book, id=book_id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart.books.add(book)
    return redirect('cart')

def cart_view(request):
    if not request.user.is_authenticated:
        return render(request, 'cart.html')
    cart, created = Cart.objects.get_or_create(user=request.user)
    books = cart.books.all()
    total_price = sum(book.price for book in books)
    return render(request, 'cart.html', {'books': books, 'total_price': total_price})

def remove_from_cart(request, book_id):
    if not request.user.is_authenticated:
        return redirect('login')
    book = get_object_or_404(Book, id=book_id)
    cart = Cart.objects.get(user=request.user)
    cart.books.remove(book)
    return redirect('cart')

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        age = request.POST['age']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        if password == confirm_password and len(password) >= 8 and len(username) <= 30 and age.isdigit() and len(age) <= 3:
            user = User.objects.create_user(username=username, password=password)
            user.save()
            return redirect('login')
    return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('home')
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect('home')

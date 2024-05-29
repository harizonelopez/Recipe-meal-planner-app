from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.http import HttpResponse
from .models import Recipe
from .forms import RecipeForm
from django.contrib.auth.decorators import login_required
from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

@login_required
def home(request):
    recipes = Recipe.objects.filter(user=request.user)
    return render(request, 'home.html', {'recipes': recipes})

@login_required
def recipe_new(request):
    if request.method == "POST":
        form = RecipeForm(request.POST)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            messages.success(request, "Recipe successfully created")
            return redirect('home')
    else:
        form = RecipeForm()
    return render(request, 'recipe_form.html', {'form': form})

@login_required
def recipe_edit(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    if request.method == "POST":
        form = RecipeForm(request.POST, instance=recipe)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.user = request.user
            recipe.save()
            messages.success(request, "Recipe successfully updated")
            return redirect('home')
    else:
        form = RecipeForm(instance=recipe)
    return render(request, 'recipe_form.html', {'form': form})

@login_required
def recipe_delete(request, pk):
    recipe = get_object_or_404(Recipe, pk=pk)
    recipe.delete()
    messages.success(request, "Recipe successfully deleted")
    return redirect('home')

@login_required
def generate_pdf(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="mealplan.pdf"'

    p = canvas.Canvas(response, pagesize=letter)
    width, height = letter
    y = height - 50

    recipes = Recipe.objects.filter(user=request.user)

    for recipe in recipes:
        p.drawString(100, y, f"Recipe: {recipe.name}")
        y -= 20
        p.drawString(100, y, "Ingredients:")
        y -= 20
        for line in recipe.ingredients.split('\n'):
            p.drawString(120, y, line)
            y -= 20
        p.drawString(100, y, "Instructions:")
        y -= 20
        for line in recipe.instructions.split('\n'):
            p.drawString(120, y, line)
            y -= 20
        y -= 40

    p.showPage()
    p.save()
    return response

def register(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = User.objects.create_user(username=username, email=email, password=password)
        user.save()    
        messages.success(request, "Account created successfully")
        return redirect('login')
    else:
        return render(request, 'register.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.warning(request, "Invalid username or password. Try again.")
            return redirect('login')
    else:
        return render(request, 'login.html', {})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, "You have successfully logged out")
    return redirect('login')

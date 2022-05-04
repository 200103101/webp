from django.shortcuts import render, redirect
from .models import Book,task,sport,test,Emp
from .forms import BookCreate,EmpForm
from django.http import HttpResponse
from django.core.exceptions import ValidationError
from main import models

def home(request):
    tasks = task.objects.all()
    return render(request, 'main/home.html',{'title': 'hello', 'tasks':tasks})
def carla(request):
    length = sport.objects.all()
    return render(request, 'main/carla.html',{'sport':length})
def about(request):
    hobby =test.objects.all()
    return render(request, 'main/about.html',{'hobby':hobby})
def last(request):
    return render(request, 'main/last.html')
def festival(request):
    return render(request, 'main/festival.html')
def Art(request):
    return render(request, 'main/Art.html')
def page(request):
    return render(request, 'main/page.html')
def end(request):
    return render(request, 'main/end.html')
def index(request):
    shelf = Book.objects.all()
    return render(request, 'main/page.html', {'shelf': shelf})
def upload(request):
    upload = BookCreate()
    if request.method == 'POST':
        upload = BookCreate(request.POST, request.FILES)
        if upload.is_valid():
            upload.save()
            return redirect('index')
        else:
            return HttpResponse("""your form is wrong, reload on <a href = "{{ url : 'index'}}">reload</a>""")
    else:
        return render(request, 'main/end.html', {'upload_form':upload})
def update_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_form = BookCreate(request.POST or None, instance = book_sel)
    if book_form.is_valid():
       book_form.save()
       return redirect('index')
    return render(request, 'main/end.html', {'upload_form':book_form})
def delete_book(request, book_id):
    book_id = int(book_id)
    try:
        book_sel = Book.objects.get(id = book_id)
    except Book.DoesNotExist:
        return redirect('index')
    book_sel.delete()
    return redirect('index')
def add_emp(request):
    if request.method == "GET":
        form = EmpForm()  
        return render(request, "main/from.html", {"form":form})
    else:
        form = EmpForm(request.POST)  
        if form.is_valid():  
            data = form.cleaned_data
            data.pop("r_salary")
            models.Emp.objects.create(**data)
            return redirect('home')
        else:  
            clear_errors = form.errors.get("all")  
            return render(request, "main/from.html", {"form": form, "clear_errors": clear_errors})

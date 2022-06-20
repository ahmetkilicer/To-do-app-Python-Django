from django.shortcuts import render,redirect
from .models import Todos
from .forms import ListForm

# Create your views here.
def index(request):
    if request.method=="POST":
        searched=request.POST['searched']
        todos=Todos.objects.filter(title__contains=searched) | Todos.objects.filter(description__contains=searched)
        return render(request,"todoapp/index.html",{"todos":todos})
    context={
        "todos":Todos.objects.all()
    }
    return render(request,"todoapp/index.html",context)

def about(request):
    return render(request,"todoapp/about.html")

def create(request):
    if request.method=="POST":
        form=ListForm(request.POST)
        if form.is_valid() :
            form.save()
            return redirect("index")
        else :
            return render(request,"todoapp/create.html",{"error":"Please enter a title!"})
    return render(request,"todoapp/create.html")

def delete(request,id):
    todo=Todos.objects.get(pk=id)
    todo.delete()
    return redirect("index")
def yes_finish(request,id):
    todo=Todos.objects.get(pk=id)
    todo.done=False
    todo.save()
    return redirect("index")
def no_finish(request,id):
    todo=Todos.objects.get(pk=id)
    todo.done=True
    todo.save()
    return redirect("index")

def update(request,id):
    todo=Todos.objects.get(pk=id)
    form=ListForm(request.POST, instance=todo)
    if request.method=="POST":
        if form.is_valid() :
            form.save()
            return redirect("index")
        else :
            return render(request,"todoapp/update.html",{"error":"Please enter a title!" , "todo":todo})
    return render (request, "todoapp/update.html" ,{"todo":todo})
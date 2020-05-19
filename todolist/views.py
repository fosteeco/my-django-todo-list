from django.shortcuts import render
from .forms import todoForm
from .models import todoItem
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import DeleteView

def home(request):
    return render(request, 'home.html')

def todohome(request):
    allitems = todoItem.objects.all()
    return render(request, 'todohome.html',{'todoitems': allitems})


def createtodo(request):
    if request.method == 'POST':
        filled_form = todoForm(request.POST)
        if filled_form.is_valid():
            created_todo = filled_form.save()
            created_todo_pk = created_todo.id
            note = 'Successfully created todo!, ID#= %d' %(created_todo_pk,)

            filled_form = todoForm()
        else:
            created_todo_pk = None
            note = 'Failed to create todo!'
        return render(request, 'createtodo.html', {'created_todo_pk': created_todo_pk, 'todoform': filled_form, 'note':note})
    else:
        form = todoForm()
        return render(request, 'createtodo.html', {'todoform': form})

def edittodo(request, id):
    gettodo= todoItem.objects.get(pk=id)
    #gettodo= todoItem.objects.all()[id]
    form = todoForm(instance=gettodo)
    if request.method == 'POST':
        filled_form = todoForm(request.POST, instance=gettodo)
        if filled_form.is_valid():
            filled_form.save()
            form = filled_form
            note = 'Todo has been updated.'
            return render(request, 'edittodo.html', {'todo': gettodo, 'todoform':form, 'note':note})
    return render(request, 'edittodo.html', {'todo': gettodo, 'todoform':form})

class deletetodo(DeleteView):
    model = todoItem
    success_url = reverse_lazy('todohome')



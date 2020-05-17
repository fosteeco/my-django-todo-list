from django.shortcuts import render
from .forms import todoForm
from .models import todoItem

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

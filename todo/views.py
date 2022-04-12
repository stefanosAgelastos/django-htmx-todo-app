from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render
from .models import Todo


def index(request):
    return render(request, 'todo/index.html', {})


def todo_list_partial(request):
    todos = Todo.objects.all()
    return render(request, 'todo/todo_list_partial.html', {'todos': todos})


def create(request):
    Todo.create(title=request.POST['title'], text=request.POST['text'])
    response = render(request, 'todo/index.html', {})
    response['HX-Redirect'] = request.META['HTTP_HX_CURRENT_URL']
    return response


def todo_details_partial(request, pk):
    todo = get_object_or_404(Todo, pk=pk)

    if request.method == 'GET':
        return render(request, 'todo/todo_details_partial.html', {'todo': todo})
    elif request.method == 'DELETE':
        todo.delete()
    elif request.method == 'PUT':
        todo.title = request.PUT[f'todo_{pk}_title']
        todo.text = request.PUT[f'todo_{pk}_text']
        todo.save()

    todos = Todo.objects.all()
    return render(request, 'todo/todo_list_partial.html', {'todos': todos})


def rerank(request):
    # print(request.POST.getlist('todo_order'))
    reranked = [int(item) for item in request.POST.getlist('todo_order')]
    Todo.rerank_by_list(reranked)
    return HttpResponse(status=204)

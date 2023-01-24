from ninja import NinjaAPI , Schema
from django.http import HttpResponse,JsonResponse
from .models import todolist
from .schema import todo_list_in
from django.shortcuts import get_object_or_404
from django.shortcuts import render

api = NinjaAPI()


   
@api.get('/get')
def index(request):
    x = todolist.objects.values()
    return JsonResponse(list(x) , safe=False)
    
@api.get('/get/{todolist_id}', response= list[todo_list_in])
def get_task(request, todolist_id : int):
    x = todolist.objects.filter( id = todolist_id)
    return x

# get_object_or_404


@api.post('/add')
def add(request, data : todo_list_in):
    data = todolist.objects.create(**data.dict())
    return JsonResponse({'id': data.id})


@api.put('/update/{todolist_id}')
def update(request, todolist_id : int, payload : todo_list_in):
    x = get_object_or_404(todolist, id = todolist_id)
    for attr, value in payload.dict().items():
        if value:
            setattr(x, attr, value)
    x.save()
    return {"success": True}


@api.delete('/delete/{todolist_id}')
def delete(request, todolist_id : int):
    x = get_object_or_404(todolist, id = todolist_id)
    x.delete()
    return {"success": True}
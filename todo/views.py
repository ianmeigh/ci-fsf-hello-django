from django.shortcuts import render
from .models import Item


# Create your views here.
def get_todo_list(request):
    items = Item.objects.all()
    fields = Item._meta.fields
    context = {"fields": fields, "items": items}
    return render(request, "todo/todo_list.html", context)

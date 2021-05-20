from django.shortcuts import render,redirect
from .models import Task
from .forms import Todoforms
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import UpdateView,DeleteView
from django.urls import reverse_lazy

# Create your views here.
class TaskListView(ListView):
    model = Task
    template_name = 'index.html'
    context_object_name = 'task'

class TaskDetailView(DetailView):
    model = Task
    template_name = 'detail.html'
    context_object_name = 'task1'

class TaskUpdateView(UpdateView):
    model = Task
    template_name = 'update.html'
    context_object_name = 'task1'
    fields = ('name', 'priority', 'date')
    def get_success_url(self):
        return reverse_lazy('cbvdetail', kwargs={'pk':self.object.id})

class TaskDeleteView(DeleteView):
    model = Task
    template_name = 'delete.html'
    success_url = reverse_lazy('cbvtask')


def index(request):

    obj1 = Task.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        priority = request.POST.get('priority')
        date = request.POST.get('date')
        obj = Task(name=name, priority=priority, date=date)
        obj.save()
        return redirect('/')
    return render(request, 'index.html', {'task':obj1})

def delete(request,id):
    obj2 = Task.objects.get(id=id)
    if request.method == 'POST':
        obj2.delete()
        return redirect('/')
    return render(request, 'delete.html', {'task':obj2})

# def update(request,id):
#     task = Task.objects.get(id=id)
#     form = Todoforms(request.POST or None, instance = task)
#     if form.is_valid():
#         form.save()
#         return redirect('/')
#     return render(request,'edit.html', {'task':task, 'form':form})


# def add(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         priority = request.POST.get('priority')
#         obj = Task(name=name, priority=priority)
#         obj.save()
#     return render(request, 'home.html')

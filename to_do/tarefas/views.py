from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from django.urls import reverse

from to_do.tarefas.forms import TarefaNovaForm


def home(request):
    if request.method == 'POST':
        form = TarefaNovaForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('tarefas:home'))
        else:
            return render(request, 'tarefas/home.html', {'form': form}, status=400)
    return render(request, 'tarefas/home.html')

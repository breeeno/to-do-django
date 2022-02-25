from django.urls import path
from to_do.tarefas import views

app_name = 'tarefas'

urlpatterns = [
    path('', views.home, name = 'home'),
    path('<int:tarefa_id>', views.detalhe, name = 'detalhe' )

]

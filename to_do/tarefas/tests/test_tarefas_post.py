import pytest
from django.urls import reverse
from to_do.tarefas.models import Tarefa

@pytest.fixture
def resposta(client, db):
    resp = client.post(reverse('tarefas:home'), data={'nome':'Tarefas'})
    return resp


def test_tarefa_existe_no_db(resposta):
    assert Tarefa.objects.exists()


def test_redirecionamento_pos_salvar(resposta):
    assert resposta.status_code == 302


@pytest.fixture
def resposta_invalida(client, db):
    resp = client.post(reverse('tarefas:home'), data={'nome':''})
    return resp


def test_tarefa_nao_existe_no_db(resposta_invalida):
    assert not Tarefa.objects.exists()


def test_pagina_com_dados_invalidos(resposta_invalida):
    assert resposta_invalida.status_code == 400